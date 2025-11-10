---
emoji: ◀️
title: Reverse Array
layout: base
description: Reverse and array
date: 2010-11-12
---


```c++
#include <cuda_runtime.h>
#include <iostream>
#include <stdio.h>

__global__ void reverse_array(float* input, int N) {
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i<N/2) {    
        std::swap(input[i],input[N-i-1]);
    }

}

// input is device pointer
extern "C" void solve(float* input, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    reverse_array<<<blocksPerGrid, threadsPerBlock>>>(input, N);
    cudaDeviceSynchronize();
}
```