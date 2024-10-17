---
emoji: 🍃
title: Gossip glomers
description: Glomming, Jepsen, and other struggles with distributed systems
date: 2024-08-08
layout: base
---



I reused the functions provided at https://github.com/jepsen-io/maelstrom/tree/main/demo/go
for interfaces.

repo: https://github.com/subygan/gg


## 1. Echo

This was a gentle intro to maelstrom and it's tools. TBF the message passing using RPC was pretty interesting. Implementing the `read()` and `write()` functions and then handing it off to the maelstrom Node made it work.

## 2. Unique Id Generation

This was fairly simple enough, I did a `uuid.NewSring()` with every request. There wasn't even any locks involved!!

## 3a. Single Broadcast.

With single broadcast, there is an assumption that there is one other node that is present. And messages need to be passed between them the signatures to implement were,

`broadcast()` to send message to other node. 

`read()` to read message from another node.

`topology()` to receive the topology of the network, which in this case was just one other node.

One interesting bug that I faced was that, golang did not copy the messages if I just did `resp.m := messages` the messages that I had were lost at a later time, because I was only storing pointers. I had to do `resp.m = make([]string, len(messages))` So that I copy all the messages from in-memory to the response to generate the response.

## 3b. Multi Broadcast.

Multi Broadcast is a challenge where 5 nodes are discussing topology, and messages withing themselves. The signatures to implement were the same as before, but the implementation was a bit more complex.
I now introduced locks because, if multiple nodes were talking with each other, then overlapping requests could cause missed data. These locks were used, when I write the message to inmemory, and when I read the message from inmemory. I used a `sync.Mutex` to implement this. But, I could used a `sync.RWMutex` to make it more efficient. so that when Reading, I don't hold a readlock. Seemed like an overkill for this implementation, as I was not optimizing for performance.


## 3c. Multi Broadcast with network partitions.

This was the most challenging exercise so far, because I had very vague hypothesis on how to get around, network partitions.

My previous implementation with `sync.Mutex` was also wrong, because due to write locks in 2 places, I ended up losing a lot more packages other than the ones that were lost due to network partitions.

I experimented a lot of ways to maintain response time, even went into an unnecessary rabbithole of optimizing the message size and stuff. But, in the end, I realized that I was not even handling the network partitions correctly.

I had to spin up multiple workers. So, that no msg is dropped. I had to receive all messages and retry and they succeed. I spun up multiple goroutines sharing the same channel, waiting to respond to messages and keep retrying until success. I was a little confused about the number of workers. Figured, 2x the number of nodes should work fine.

I used the standard setup for spinning up multiple workers.

```go
	for i := 0; i < worker; i++ { //Start workers
		go func() { // create a goroutine per worker
            for {
                select {
                case msg := <-ch:
                // do something with the message
				case <-ctx.Done():
				//	Handle ctx ending
                }
			}
        }	
```

And it worked!!!❣️

There was a bug, where the `sync.Mutex` lock was deferring and waiting until the end of the call stack and ending up choking the whole system. But, I ironed it out pretty quickly. Good reminder that locks need to be used sharp, localized, and atomic. Like, a Scalpel.     


### 3d. Efficient Broadcast 

Efficient broadcast was kinda counterintuitive, because there were 25 nodes.
I had to spawn completely new routines per request. instead of having workers per server as this model scales the number of workers based on the messages to be sent.

"Efficient messages" also means that storing the messages efficiently. The biggest problem was that all my messages were in a huge append-only style list. Which made it very inefficient when sending because of the repeated messages. I converted that into a map so that I save every message only once.

I also stored the topology and then filtered the nodes to send message based on that.

I read through the whole maelstrom document from echo to efficient broadcast, to understand what was happening. the `store/latest` page is incredibly useful when each thing is understood properly. the messages.svg is just 🤌🏻 perfect.


## 3e. Efficient Broadcast ++

The challenge was to implement the system such that, there were 20 msgs-per-op and median latency below 1s and 99th percentile below 2s.

This worked smoothly without even any code change because with problem 3d, I ran it with network partition and bought the response time much lower. My implementation still did it in under 150ms 95 %ile and 180ms 100%ile. I was pretty happy with the results.

## 4. Grow Only Counter

Grow only counters usually have only one operation `add`. Everything else is used to keep it consistent.

Maelstrom itself comes with a neat implementation for a [`sequentially consistent`](./sequential_consistency) key value store.

The setup is such that, each node is given a KV and needs to always respond with the total of all values so far. For this, the nodes need to confer with each other ot know what values the other nodes have seen.

As a developer I understand that Debugging needs going through a lot of logs. But in this case, I needed to understand maelstrom's logging system (which is spectacular BTW).

But, reading it helped a lot `messages.svg` from the logs made it obvious that I forgot to instantiate the key with some value in the beginning and, maelstrom deviously was reading before it had written anything.

The discussion logic between nodes was quite interesting to implement.






