# Problem: 39. Combination Sum

## Problem Summary
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times.

## Approach
I first created a dfs function that would take in an array and its sum. If the sum is equal to the  target value, it is appended to the return list. Otherwise, the function runs through all the values in the candidates list: if it is less than or equal to the target-sum (meaning adding it to the sum will be less than or equal to the target) and it is greater than or equal to the last element of the temporary list (meaning that the list is sorted in ascending order and duplicate arrays aren't  returned). Finally, I call the function with the initial parameters [] and 0, and then return the  rlist.

## Complexity Analysis
- Time Complexity:  O(n^(t/m)), n = number of candidates, t = target value, m = minimum candidate value
- Space Complexity: O(t/m)