---
title: Min in Rotated Array 
date: 2023-11-26
layout: base
tags: ["tech", "programming"]
---

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.


## Solution

On first look, it is easy to observe this should only be O(n).
But, since it is a sorted array, ideally we should be able to do this in O(log n).

if we imagine the array to be circular list joined at the highest and lowest value. we can select any to adjacent values (call them `l` and `r`), it is provable that apart from the exact join, `l<r`. 
if we find a for these, the middle point(`m`), it would be the diametrically opposite value. Now, with this, there are 3 possible cases.

- middle value is less than the right value. This means, the minimum is on the left side. so we make `r=m`
- middle value is greater than the right value. This means, the minimum is on the right side. so we make `l=m`
- middle value is equal to the right value. we don't know which side. so we make `r=r-1`. This means that, the true O() value is still O(n) because in the worst case where all elements are the same, we will have to traverse the entire array. but, in every other case it is O(log n).

{{% code file="/tech/algos/problems/leetcode/154_min_in_rotated_arr.cpp" language="cpp" %}}

