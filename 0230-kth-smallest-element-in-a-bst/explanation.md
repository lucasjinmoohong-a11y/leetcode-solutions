# Problem: 230. Kth Smallest Element in a BST

## Problem Summary
Return the kth smallest element in a BST.

## Approach
I first created an in-order traversal that would run through all elements of the BST in-order. As this occured, elements would be appended to a list. Finally, the code would return the (k-1) indexed element in the list, because it is finding the kth smallest element in the BST.

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)
