# Problem: 701. Insert into a Binary Search Tree

## Problem Summary
Insert a value into a BST such that the BST remains a BST after insertion.

## Approach
I first ran through the binary tree by mimicking a search function; this would ensure that the final position of the given insertion value would be in the right place for the BST to remain sorted afterwards. After arriving at a Null value, I would use the previous node of the Null node and compare it to val; placing it accordingly, I would return the root node. 

However, this code had the issue of not working when the root node was Null. To fix this, I implemented an edge-case in my final code that returned a new TreeNode with the given value 'val.'

## Complexity Analysis
- Time Complexity: O(log(n))
- Space Complexity: O(1)

## Reflections
In the future, think about edge-cases when coding; often, code doesn't work when there are 0 values or just 1, so add edge-cases to ensure your code runs smoothly in all cases. 