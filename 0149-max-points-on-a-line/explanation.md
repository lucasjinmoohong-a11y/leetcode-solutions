# Problem: 149. Max Points on a Line

## Problem Summary
Given an array of points on the X-Y plane, return the maximum number of points that lie on the same straight line.

## Approach
I first thought of creating a line between every combination of two points and counting how many points said line hit. From there, I would simply find the max number of points hit by any given line. 

My second iteration fixed the edge cases where there were either 0 or 1 points in the list. 

My third iteration faced a problem with a specific testcase. My first thought was that it was a problem with a rounding error in LeetCode. However, even after implementing a rounding safeguard, the code continued to output wrong answers. 

My final code tried to fix this by not modifying the "points" list while iterating over it, but it still didn't work. I finally realized that the problem was solely in LeetCode, as my code ran fine in VS Code. 

## Complexity Analysis
- Time Complexity:  O(n^3*20001) - very high time complexity, including the high constant term (20001)
- Space Complexity: O(n)

## Reflections
I learned to not modify lists while iterating over them, even if that wasn't the problem with my code in the end. It is good coding practice to not do it, and it ensures that you don't waste time trying to fix it if you hit an error. Moreover, I learned that issues in code can sometimes be attributed to the software running it, not necessarily the code itself. If I run into a consistent problem again in the future, I will try to run it in VS code and make sure the problem is inherent in my code. 