# Problem: 199. Binary Tree Right-Side View

## Problem Summary
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Approach
I first created a BFS with an added caveat: instead of popping elements from the front of the queue, it would pop elements from the end of the queue. Moreover, elements would only be appended to the return list if it was the first element in the level. 

However, this had one key problem: because the BFS was popping elements from the end of the queue, it would be appending elements in the wrong order; rather than appending elements left-to-right within one layer, it would append the left child's children before appending the right child. 

My final solution solved this by implementing a more traditional BFS, with a temporary list made each layer. From there, the only element that would be appended to the return list would be the final element of the temp list. 

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)

## Reflections
I learned that you must be careful when making changes to algorithms; in this case, by changing the BFS from a FIFO to a FILO system, I completely changed the order in which elements would be appended to the return list, which meant that my modifications to the algorithm just didn't work at all. 