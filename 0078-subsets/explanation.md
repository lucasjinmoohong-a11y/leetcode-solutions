# Problem: 78. Subsets

## Problem Summary
Given an integer array nums of unique elements, return all possible unique subsets.

## Approach
My first thought was to create a helper function that would recursively create new subsets and append them to the return list. I appended None to nums to account for the case in which a subset would end without adding another element. From there, I ran a function that would intake a subset and check if its last element was None. If it was, it would be appended to the return list without the None. Otherwise, every element in nums would be appended to it, as long as it was not already in the subset.

However, there were two main issues with this: 
1. There would only be a maximum of len(nums) items in the return list because the outer loop that would call the helper function was bounded by the number of elements in nums. 
2. appending the subset simply didn't work in the code, as it just became null. 

To fix this, I first reworked my code to include the appending of the subset to the return list within the recursive function, rather than in the main code. This would ensure that the number of subsets wouldn't be bounded by the number of elements in nums. Next, I included the case of the empty list at the end of my code, instead opting to include the case where subsets stop adding new elements in the helper function. Finally, I created a temporary copy of the subset between each adding of a new element to the subset. This would ensure that not all elements would be added to a subset at once.

One problem persisted, however. The code repeats elements multiple times; instead of each combination of x elements, it takes each permutation of them.

In my final code, I added ordering to my subsets by adding another conditional to the adding of a new element to a subset; the new element would have to be greater than the last element of the subset. Because the code is recursive, this means that it would have to be the max element of the list, and the list would be ordered in ascending fashion. This took away all duplicates.

## Complexity Analysis
- Time Complexity: O(n*2^n)
- Space Complexity: O(n*2^n)

## Reflections
I got more experience with implementing recursion, and I learned about how to implement helper functions. Moreover, I also learned to be more careful when iterating; changes to the same object persist throughout iterations, so you need to create temporary copies if you want to make different chages to the same object each time. 