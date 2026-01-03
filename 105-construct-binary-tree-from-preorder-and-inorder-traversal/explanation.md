# Problem: 105. Construct Binary Tree from Preorder and Inorder Traversal

## Problem Summary
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Approach
I immediately tried to make a recursive function, because I realized that the process of building a tree would be the same whether it was the full tree or a subtree; all that had to be changed were the preorder/inorder lists. I first tried to only change the preorder list. I partitioned the preorder lists about the root node and recursively called the function again for the left and right children of the root. Finally, the code would return the current node. 

However, this code had multiple issues. In my final code, I first fixed the partition logic using slicing. I found the index of the root node within inorder and used it to partition the inorder list into the right and left subtree's inorder list. Next, I partitioned the preorder list by making the left subtree's preorder list the first idx-1 elements after the root node, and leaving the rest as the right subtree's preorder list. Finaly, I then got rid of the subtree function because it was unnecessary and could have just been put in the buildTree() function.

## Complexity Analysis
- Time Complexity: O(n^2)
- Space Complexity: O(n^2)

## Reflections
I got more practice with recursive functions: how to recognize when to use them, and how to implement them without the use of helper functions. Instead of trying to initialize something within a separate function and then calling the recursive function, I could have just done it all within the recursive function.