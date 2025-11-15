---
emoji: ©️
title: matrix copy
layout: base
description: Copy the matrix
date: 2025-11-12
---


```c++
#include <cuda_runtime.h>
#include <stdio.h>
#include <iostream>

__global__ void copy_matrix_kernel(const float* A, float* B, int N) {
    int idx = blockDim.x* blockIdx.x + threadIdx.x;
    if (idx<N){

        B[idx] = A[idx];
    } 

}

// A, B are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, float* B, int N) {
    int total = N * N;
    int threadsPerBlock = 256;
    int blocksPerGrid = (total + threadsPerBlock - 1) / threadsPerBlock;
    copy_matrix_kernel<<<blocksPerGrid, threadsPerBlock>>>(A, B, total);
    cudaDeviceSynchronize();
} 
```