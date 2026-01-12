---
emoji: 🔄
title: SiLu
layout: base
description: count
date: 2025-11-12
tags: ["tech", "programming", "machine-learning"]
---


```cpp
#include <cuda_runtime.h>

__global__ void silu_kernel(const float* input, float* output, int N) {
    int id = blockDim.x * blockIdx.x + threadIdx.x;

    if (id<N) output[id] = input[id]*(1/(1+std::exp(-1*(input[id]))));

}

// input, output are device pointers
extern "C" void solve(const float* input, float* output, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    silu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N);
    cudaDeviceSynchronize();
}


```