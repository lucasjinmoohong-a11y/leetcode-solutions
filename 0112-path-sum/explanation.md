# Problem: 112. Path Sum

## Problem Summary
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

## Approach
I created a helper function that would run through all root-leaf paths and return True if one worked. I did this through recursion; the root would be added to a 'sum' variable, which was compared to the targetSum; if they were equal and it was a leaf node, the function would return True. Otherwise: it would return False. It would then try running the function on the root's children; if both were False the function would return False. Otherwise: it would return True. 

However, this didn't work for negative elements. In my final solution, I removed the "if sum > targetSum: return False." 

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(log(n))

## Reflections
I was reminded that elements in a binary tree can be negative.