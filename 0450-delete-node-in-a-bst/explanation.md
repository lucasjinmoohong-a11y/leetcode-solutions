# Problem: 450. Delete Node in a BST

## Problem Summary
In a BST, delete a node such that the BST remains a BST afterwards.

## Approach
My first attempt centered around finding the key node first and deleting it second. However, I realized the challenge in trying to delete a node using just the node itself; even if I set the node's value to None, its structure would still remain in the BST, and the code would fail. I tried creating a 'prev' variable to keep track of the node previous to the current node. This would have allowed me to simply change the previous node's pointer to None to delete the current node. However, this came with a lot of complications and edge-cases, so I decided to abandon my approach and try again. 

My second attempt centered around a recursive approach that took things one step at a time. Instead of running a while loop to find the key node, the code would simply rerun the function on the node's child (either left or right). Then, when it found the key node, the code would split into 4 possible scenarios: First, if neither root.left or root.right exist, then it returns None (meaning that the pointer pointing to the node now points to None). If only one exists, then it returns it (meaning the pointer now points to the remaining child and skips the current node). If both exist, then it finds the smallest node greater than the current node and replaces the current node with it. Then, it calls the function again on the right subtree (so that it deletes the other copy of the value
you replaced the key with). Finally, the code returns root. By running the code recursively, the code removed the need to keep track of a prev value. 

## Complexity Analysis
- Time Complexity: O(h), h = height of the BST
- Space Complexity: O(h)

## Reflections
I learned two things. First, I learned the value of running recursive functions; by running things recursively rather than in a while loop, it allowed me to keep track of fewer values and do things step-by-step. Second, I learned that finding a target node is not sufficient to changing the structure of the BST (or one-way linked list) around the node. Instead, I should either implement recursion or keep track of the previous node. 