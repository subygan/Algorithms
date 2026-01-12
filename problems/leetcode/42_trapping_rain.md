---
emoji: 🌧️
title: 42. Trapping Rain Water
date: 2023-11-26
layout: base
tags: ["tech", "programming"]
---

## Problem Statement
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Solution

- The key insight is that, When both extremes are high, water traps between them. and the height of water is always going to be the lower of the two extremes. this is true even if there is something that is higher than the current one, in between.
- So, a two pointer search from both ends, moving the lower value forward will work.

{{% code file="/tech/algos/problems/leetcode/42_trapping_rain.cpp" language="cpp" %}}