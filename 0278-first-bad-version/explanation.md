# Problem: 278. First Bad Version

## Problem Summary
In a list of numbers 1 to n, there are 'bad versions' within this list such that for each 'bad version,' each subsequent number is also a 'bad version.' Find the first 'bad version' in the list, given a function that checks whether a number is a 'bad version.'

## Approach
I created a binary search algorithm that ran while the left pointer was less than or equal to the right
pointer. The algorithm created a middle pointer and checked whether or not it was a bad version. If it
was, it would set it as the first bad version (so far) and change the right pointer to mid - 1. If not,
it would set the left pointer to mid + 1. After left > right, it returned first. 

## Complexity Analysis
- Time Complexity: O(log(n))
- Space Complexity: O(1)