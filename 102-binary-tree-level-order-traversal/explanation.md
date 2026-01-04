# Problem: 102. Binary Tree Level-Order Traversal

## Problem Summary
Given the root of a binary tree, return the level order traversal of its nodes' values. For each level of the tree, create a separate sublist in the return list.

## Approach
I implemented a BFS, where values would be stored in a queue and appended to the return list in the
order they were appended. However, I added a temporary list between each level of the tree and added
the node values in the corresponding level to the temporary list first before appending the temp
list to the return list.

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)