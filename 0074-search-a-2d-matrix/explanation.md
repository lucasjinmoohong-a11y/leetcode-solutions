# Problem: 74. Search a 2D Matrix

## Problem Summary
Given an m x n sorted (ascending order) matrix, use a binary search algorithm to find a target value. Return True if it is in the matrix, False if not.

## Approach
My solution comprised of two parts; search for the correct row, and then search for the correct value. I first created pointers for the top/bottom row and the left/right element of each row. From there, 
while top < bottom (ie top != bottom), I would calculate the middle row and compare its first element
to the target value. If it was greater than the target, the bottom pointer would be pushed up to mrow
(not mrow - 1 because that could go out of bounds). If it was less than the target, the top pointer
would be pushed to mrow + 1. Finally, if they were equal, then I would have found the right value. 

From there, after I found the right row, the code would run a binary search algorithm within the row. 

However, this yielded incorrect answers, because I was comparing the wrong elements when searching for the correct row. Rather than checking the first element of mrow each time, I changed it to checking the first element if seeing whether it was larger than the target and checking the last element if seeing if it was smaller than the target. This was because, if mrow was already the correct row, my previous solution ran the risk of bypassing it simply because the target was not the first value. Moreover, if neither conditionals were True, then the value must be in mrow, so I set both top/bottom to mrow. The binary search within the row remained the same.

## Complexity Analysis
- Time Complexity: O(m * n)
- Space Complexity: O(1)

## Reflections
I learned not to rely on past experience / memorized formats for algorithms, because they can sometimes prove incorrect in new contexts. Instead, I should use it as a basic skeleton to guide my thinking, while checking each step to make sure it makes sense. In this case, I should have made sure I was checking the right elements in mrow, rather than defaulting to the first element. 