---
emoji: ✚
title: Vector Addition
layout: base
description: Adding two similar shaped vectors
date: 2025-11-12
tags: ["tech", "programming", "machine-learning"]
---

The question was

```
Implement a program that performs element-wise addition of two vectors containing 32-bit floating point numbers on a GPU. The program should take two input vectors of equal length and produce a single output vector containing their sum.

Implementation Requirements
External libraries are not permitted
The solve function signature must remain unchanged
The final result must be stored in vector C
```


Identifying the thread uniquely is always done like using
`blockIdx.x * blockDim.x + threadIdx.x`

all of these are three dimensional variables, so if a threedimensional block was installed we get three dimensional values.




```cpp
#include <cuda_runtime.h>

__global__ void vector_add(const float* A, const float* B, float* C, int N) {

    int i = blockIdx.x * blockDim.x + threadIdx.x; 
    if (i<N) C[i] = A[i] + B[i];
}

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* C, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    vector_add<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, N);
    cudaDeviceSynchronize();
}

```
