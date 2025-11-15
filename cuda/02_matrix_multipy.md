---
emoji: X
title: Matrix Multiply
layout: base
description: multiplying two simple matrices
date: 2025-11-12
---

The tricky part in this was that, I took some time to intuit that each thread should associate to each value in the output matrix.

and then I'll have to iterate. 


```cpp
#include <cuda_runtime.h>
#include <stdio.h>
#include <iostream>

__global__ void matrix_multiplication_kernel(const float* A, const float* B, float* C, int M, int N, int K) {

    int k = (blockIdx.x * blockDim.x + threadIdx.x); //uniquely identify a row
    int m = (blockIdx.y * blockDim.y + threadIdx.y); //uniquely identify a column
    
    if ( m<M && k<K) {
        float total = 0.0;

        for (int i = 0; i<N;++i){
            total +=A[m*N+i] * B[i*K+k];
        }

        C[m*K+ k] = total;
    }

}

// 1.0 2.0     5.0 6.0
// 3.0 4.0     7.0 8.0

// 1.0,2.0,3.0,4.0   5.0,6.0,7.0, 8.0

// 1*(5+7)
// 2*(6+8)
// 3*(5+7)
// 4*(6+8)

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* C, int M, int N, int K) {
    dim3 threadsPerBlock(16, 16);
    dim3 blocksPerGrid((K + threadsPerBlock.x - 1) / threadsPerBlock.x,
                       (M + threadsPerBlock.y - 1) / threadsPerBlock.y);
    
    matrix_multiplication_kernel<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, M, N, K);
    cudaDeviceSynchronize();
}
```