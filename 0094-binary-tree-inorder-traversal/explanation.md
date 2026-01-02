# Problem: 94. Binary Tree Inorder Transversal

## Problem Summary
Given the root of a binary tree, return the inorder traversal of its nodes' values.

## Approach
I created a recursively called function inorder() that would run the root's left child first (because 
it is less than the root), then the root itself, and then the root's right child. Because it is called
recusively, it will run the node furthest left first and go in-order from there. To track these values,
I created an empty list rlist that would be appended to during inorder(). Finally, rlsit was returned.

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)

## Reflections
When running a recursive function, it is sometimes better to create a helper function that modifies a global variable to ensure the variable isn't constantly initialized. 