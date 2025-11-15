---
emoji: 🔄
title: SwiLu
layout: base
description: Swish Gated Linear Unit
date: 2025-11-12
---


```c++
#include <cuda_runtime.h>

float silu(float x){
    return x*(1/(1+std::exp(-1*(x))));
}

__global__ void swiglu_kernel(const float* input, float* output, int halfN) {

    int id = blockDim.x * blockIdx.x + threadIdx.x;

    if(id<halfN) output[id] = input[id%halfN]*(1/(1+std::exp(-1*(input[id%halfN])))) * input[id%halfN + halfN];

}

// input, output are device pointers
extern "C" void solve(const float* input, float* output, int N) {
    int halfN = N / 2;
    int threadsPerBlock = 256;
    int blocksPerGrid = (halfN + threadsPerBlock - 1) / threadsPerBlock;

    swiglu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, halfN);
    cudaDeviceSynchronize();
}
```