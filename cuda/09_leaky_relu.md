---
emoji: ◀️
title: Leaky ReLu
layout: base
description: Applying ReLu to an array
date: 2025-11-12
tags: ["tech", "programming", "machine-learning"]
---



```c++
#include <cuda_runtime.h>

__global__ void leaky_relu_kernel(const float* input, float* output, int N) {
    int id = blockDim.x* blockIdx.x + threadIdx.x;
    if (id<N) output[id] = input[id]>0? input[id] : 0.01*input[id];

}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* input, float* output, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
    
    leaky_relu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N);
    cudaDeviceSynchronize();
}

```