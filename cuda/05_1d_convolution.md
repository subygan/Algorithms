---
emoji: []
title: 1D convolution
layout: base
description: convolving an 1D matrix
date: 2010-11-12
---


```cpp
#include <cuda_runtime.h>
#include <iostream>
#include <stdio.h>

__global__ void convolution_1d_kernel(const float* input, const float* kernel, float* output,
                                      int input_size, int kernel_size) {

    int i = blockDim.x  * blockIdx.x + threadIdx.x;
    int output_size = input_size - kernel_size +1;

    if (i < output_size ) {
        float sum = 0.0f;
        for ( int j = 0; j<kernel_size; j++) {
            sum += input[i+j]*kernel[j];
        }

        output[i] = sum;
    }


}

// input, kernel, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* input, const float* kernel, float* output, int input_size, int kernel_size) {
    int output_size = input_size - kernel_size + 1;
    int threadsPerBlock = 256;
    int blocksPerGrid = (output_size + threadsPerBlock - 1) / threadsPerBlock;

    convolution_1d_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, kernel, output, input_size, kernel_size);
    cudaDeviceSynchronize();
}
```