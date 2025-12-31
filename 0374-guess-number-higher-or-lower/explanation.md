# Problem: 374. Guess Number Higher or Lower

## Problem Summary
There is a target number x from 1 to n. Find x using a given guess() function: if your guess is less than x, it outputs 1; if your guess is greater than x, it outputs -1; else: it outputs 0.

## Approach
I recognized this as a binary search problem. I set a bottom and top pointer. While True, I set a middle pointer and compared it to the target value using the guess() function. If it was greater than the target, I moved the top pointer down to mid - 1. If it was smaller, then move the bottom pointer up to mid + 1. If mid == target, then I returned mid.

## Complexity Analysis
- Time Complexity: O(log(n))
- Space Complexity: O(1)