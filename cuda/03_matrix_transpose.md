---
emoji: T
title: Matrix Transpose
layout: base
description: Problem transposing two matrices
date: 2025-11-12
tags: ["tech", "programming", "machine-learning"]
---




```cpp
#include <cuda_runtime.h>
#include <iostream>
#include <stdio.h>

__global__ void matrix_transpose_kernel(const float* input, float* output, int rows, int cols) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int j = blockIdx.y * blockDim.y + threadIdx.y;
    printf("%d",i);

    if (i<rows && j<cols){
        output[j*rows+i] = input[i*cols+j];
    }
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* input, float* output, int rows, int cols) {
    dim3 threadsPerBlock(16, 16);
    dim3 blocksPerGrid((cols + threadsPerBlock.x - 1) / threadsPerBlock.x,
                       (rows + threadsPerBlock.y - 1) / threadsPerBlock.y);

    matrix_transpose_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, rows, cols);
    cudaDeviceSynchronize();
}
```