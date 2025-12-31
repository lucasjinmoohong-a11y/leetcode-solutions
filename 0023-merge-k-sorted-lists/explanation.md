# Problem: 23. Merge K Sorted Lists

## Problem Summary
Given k sorted linked lists in a list 'lists,' merge all of the lists into one sorted (ascending order) linked lists and return the result.

## Approach
I first created a function that merges two given lists in ascending order. This was achieved by creating a dummy node and then adding individual nodes one-by-one onto the dummy node. Nodes were added by first checking if the values existed; if they did, they were compared, and the smaller one was added onto the dummy node. If only one existed, it was automatically added onto the dummy node. After none existed, the dummy node was returned. 

This process was repeated for every pair of lists in the "lists" list, in which the merged list of the 
first two lists was appended to "lists" and the original two lists were deleted. Once only one list remained, the final list was returned. If none existed, then an empty list was returned.

However, the code faced two issues upon running; first, an empty list was not accepted, because it didn't match the required return type. Moreover, the answer for tests were incorrect; 0s were added onto the front, and the last elements of some of the lists were ignored.  

My second iteration fixed the first problem by returning None instead of []. Next, I returned
the next node after the dummy node in the mergeTwoLists() function instead of the dummy node itself to ensure that the default 0 that the dummy node was set to was not included in the final result. 

My final iteration fixed the omitted last elements of the lists by changing the conditionals in mergeTwoLists() from checking if l1.next/l2.next existed to whether l1/l2 existed, because l1 = l1.next still works even if l1.next == None, and this method ensures the last element in the list is not left out.

## Complexity Analysis
- Time Complexity:  O(kN), k = number of lists, N = total number of listNodes within all lists
- Space Complexity: O(1)

## Reflections
I learned that ListNodes could be set to None. Moreover, I learned to visualize solutions to ensure edge cases were accounted for; in this case, the edge case of the last element was omitted, because my code stopped at the second-to-last element rather than the last one. 