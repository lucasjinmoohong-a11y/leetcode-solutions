# Problem: 75. Sort Colors

## Problem Summary
Sort the list 'nums' in-place in ascending order. 'nums' only has values 0, 1, and 2, where each represents a color (0 for red, 1 for white, 2 for blue). Sort without using sort().

## Approach
I immediately recognized the problem as bucket sort due to the fixed range of the problem (just 0, 1, and 2). From there, I created buckets for each color. I ran through the nums list and added one to the corresponding counter for each color. I then created a pointer at the start of the 'nums' list. For each color, I changed the 'nums' value at the pointer to the color, and then incremented the pointer by one. I did this process the number of times shown by the corresponding counter in the buckets list. 

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Reflections
I learned how to recognize what sorting algorithm to use depending on the problem; in this case, it was good that I recognized the value in using bucket sort because it didn't require much extra memory and was incredibly time-efficient.