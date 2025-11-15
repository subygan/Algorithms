---
emoji: 🔄
title: Count Array Element
layout: base
description: count
date: 2025-11-12
---


```c++
#include <cuda_runtime.h>

__global__ void count_equal_kernel(const int* input, int* output, int N, int K) {

    int id=blockDim.x * blockIdx.x + threadIdx.x;

    if(id<N && input[id]==K) atomicAdd(output, 1);
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const int* input, int* output, int N, int K) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    count_equal_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N, K);
    cudaDeviceSynchronize();
}
```