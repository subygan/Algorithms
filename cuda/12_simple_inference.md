---
emoji: ©️
title: simple inference
layout: base
description: inference in pytorch
date: 2025-11-12
tags: ["tech", "programming", "machine-learning"]
---


```python
import torch
import torch.nn as nn

# input, model, and output are on the GPU
def solve(input: torch.Tensor, model: nn.Module, output: torch.Tensor):
    model.eval()
    with torch.no_grad():
        output.copy_(model(input))

```