# Problem: 7. Reverse Integer

## Problem Summary
Given a signed 32 bit integer x, return x with its digits reversed. If the input is greater than a 
32 bit integer, then return 0.

## Approach
I first converted the unsigned integer to a list so that the place value and digit value of each digit
would be easily accessible. From there, I created a "total" variable, which I added to using the   digit/place value of each item in the list. By adjusting the place value using the index of each digit, I was able to reverse the digits of the integer. From there, I simply used the sign of the input to get the sign of the output and returned "total." However, this approach failed to implement the edge case, where the integer is greater than 32-bit. 

My second iteration implemented this edge case by simply finding whether or not "total" was greater than 2^31-1 and returning 0 if that was the case. However, the code still didn't work, because the  index() function I was using only took the first instance of the value I was adding to "total," not the actual index. 

My final iteration fixed this by enumerating the list, which would store the value and index together. This solved the index-mismatch while reducing my time complexity from O(n) to O(n^2), because the new code didn't have to go through the list again trying to find the index. 

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)

## Reflections
Reread the problem to make sure edge cases are properly accounted for. Moreover, keep your code efficient; if you are able to store two connected values at the same time without sacrificing too much space complexity, do it in order to ensure values are stored properly and efficiently. 