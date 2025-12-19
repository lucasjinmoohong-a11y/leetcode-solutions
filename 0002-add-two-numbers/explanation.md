# Problem: 2. Add Two Numbers

## Problem Summary
Intake two linked lists. The "value" of each linked list is equal to the sum of its values, where the place value of each value is simply the index of the number. 

For example, [3,4,2] --> 3+40+200=243.

Return a new linked list that represents the value of the sum of the two input linked lists.

## Approach
My first approach was to convert each given list into an integer, add the integers together, and then turn the sum into a string. From there, I would be able to split the string into a list and return it. The problem with this approach, however, is that not only are the input linked lists not lists at all, but also that the output must also be a linked list. 

My next approach focused on fixing the len function so that we could find the length of a linked list, however this didn't fix the underlying problem. 

My third solution attempted to create a ListNode class, but it exceeded the given memory limit for the problem. 

My final attempt created a LinkedList class in addition to the ListNode class with functions that could easily add new nodes. The problem was, however, that I was supposed to use the given ListNode class from LeetCode rather than make my own. 

## Complexity Analysis
- Time Complexity: O(max(n,m))
- Space Complexity: O(max(n,m))

## Reflections
The first thing I learned was to research more on new concepts before tackling a new problem. The concept of linked lists was completely new to me, and I made a lot of mistakes regarding implementing them in my code, especially in the format wanted by LeetCode. 

The second thing I learned was that a better approach to coding is sometimes to take steps one-by-one rather than compiling all the data and attempting to use it from there. Using data as you pass through it would minimize the memory used, decrease the time taken, and make the code both simpler and easier to write. 

An alternative approach (shown in proper_solution.py in this folder) would be to create a linked list in the same way one approaches addition on paper. Rather than try to convert a list into a linked list, a better approach would be to add digits one-by-one, keeping track of the quotient and remainder. From there, one can simply create a new listNode using the remainder and add the quotient to the next sum of digits. 