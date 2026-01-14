---
emoji: 🧵 
title: cuda
description: Solving CuDa problems.
date: 2023-03-14
---


Optimizing for Concurency has always been painful for a ton of reasons. SIMD is one such thing that helps in solving this problem. Cuda kinda follows SIMT(Singl Instruction Multiple threads).
This is just a way to segment compute by the number of available threads and then vastly increasing the number of threads. instead of making it dependent on the data, which could be dynamic and constrain hardware optimization.

This has worked incredibly well for at least one company who seems to be seeing no end to the growing.


### atomicadd(valueaddress,increment)

this is a function that syncs a value across all threads and increments it by a value. quite helpful when trying to sync a value across different threads. but when the process is very shallow (eg. add values in a list) it's not very useful becuase instead of doing any useful work, all the threads are simply waiting on each other.