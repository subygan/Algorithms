---
emoji: 🧵 
title: Cuda
description: Solving CuDa problems.
date: 2023-03-14
---


Optimizing for Concurency has always been painful for a ton of reasons. SIMD is one such thing that helps in solving this problem. Cuda kinda follows SIMT(Singl Instruction Multiple threads).
This is just a way to segment compute by the number of available threads and then vastly increasing the number of threads. instead of making it dependent on the data, which could be dynamic and constrain hardware optimization.

This has worked incredibly well for at least one company who seems to be seeing no end to the growing.
