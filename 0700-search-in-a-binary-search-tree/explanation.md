# Problem: 700. Search in a Binary Search Tree

## Problem Summary
Given a Binary Search Tree, find a target value while minimizing the time complexity. 

## Approach
I created a recursive function that checks whether or not the target value == the current Node's value.
If it is, then it returns the node; if the target is larger, it goes to the Node's right child; if it 
is smaller, it goes to the Node's left child. It runs the function on the new node; if the node doesn't
exist, then it returns None because the target value is not in the tree. 

There was an issue with my first solution that made it only return None due to a problem in the recursive logic. However, I was able to quickly fix this by adding a 'return' before the function call.

## Complexity Analysis
- Time Complexity: O(log(n))
- Space Complexity: O(1)

## Reflections
I learned how to properly implement recursive functions; you must do 'return function().'