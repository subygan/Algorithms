---
title: bloom filter
emoji: 🌺
layout: base
description: Bloom filters are cool!
date: 2022-11-12
tags: ["tech"]
---

Bloom filters have nothing to do with flowers (despite the blog emoji 🥸). It was conceived by Burton howard Bloom. This is a _Space-efficient probablistic data structure_. In Bloom filter false positives are very much possible, but false-negatives are not possible (i.e.) a query either returns, "possibly in set" or "definitely not". So, when a bloom filter returns "no" you can believe it, if it returns "maybe" you cannot. And it is very very efficient.

For example in a DB, if we want to check whether a data is present, instead of making a full db check we could use bloom filter as a preliminary test to verify whether some data _could_ be in the database

A simple example of a bloom filter would be:

{{% code file="/tech/algos/bloom.go" language="go" %}}



This is used in [chromium](https://chromium.googlesource.com/chromium/blink/+/refs/heads/main/Source/wtf/BloomFilter.h) to check for malicious sites.



### refs:
- [https://llimllib.github.io/bloomfilter-tutorial/](https://llimllib.github.io/bloomfilter-tutorial/)
- [Bloom filters in chromium](https://web.archive.org/web/20180814074719/http://blog.alexyakunin.com:80/2010/03/nice-bloom-filter-application.html)