---
emoji: ◀️
title: ReLu
layout: base
description: Applying ReLu to an array
date: 2025-11-12
---




`ReLU(x) = max(0,x)`


```c++

#include <cuda_runtime.h>

__global__ void relu_kernel(const float* input, float* output, int N) {

    int id = blockDim.x* blockIdx.x  + threadIdx.x;
    if (id<N) output[id] = std::max(0.0f,input[id]);

}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* input, float* output, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    relu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N);
    cudaDeviceSynchronize();
}

```

