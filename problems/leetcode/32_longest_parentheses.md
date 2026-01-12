---
emoji: ()
title: Longest Valid Parentheses
description: given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
date: 2023-11-24
layout: base
tags: ["tech", "programming"]
---
problem link: https://leetcode.com/problems/longest-valid-parentheses/

Typically, in the parentheses problem a stack is the obvious choice. I spent too much time, chasing a phantom solution by thinking about this as a DP problem and filling various arrays.

But, then This is similar to having a stack of positions of the previous `(` positions and then just, popping them off when we encounter a `)` and also maintaining a max value, with the difference between the current position and the top of the stack.

We keep track of the last valid position, by pushing -1 to the stack initially. if we reach the bottom, we do a `stk.empty()` check and then push the current position to the stack. This makes sure that, we are the latest valid position, when we encounter a `)`.


{{% code file="/tech/algos/problems/leetcode/32_longest_parentheses.cpp" language="cpp" %}}
