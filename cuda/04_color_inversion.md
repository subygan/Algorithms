---
emoji: ✚
title: color inversion
description: Inverting color in an image.
layout: base
date: 2025-11-12
tags: ["tech", "programming", "machine-learning"]
---


```cpp
#include <cuda_runtime.h>

__global__ void invert_kernel(unsigned char* image, int width, int height) {

    int i = blockIdx.x * blockDim.x + threadIdx.x;

    image[i*4] = 255 - image[i*4];
    image[i*4+1] = 255 - image[i*4+1];
    image[i*4+2] = 255 - image[i*4+2];

}
// image_input, image_output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(unsigned char* image, int width, int height) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (width * height + threadsPerBlock - 1) / threadsPerBlock;

    invert_kernel<<<blocksPerGrid, threadsPerBlock>>>(image, width, height);
    cudaDeviceSynchronize();
}
```