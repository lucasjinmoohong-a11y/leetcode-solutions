# Problem: 1.Two Sum

## Problem Summary
I had to find the indexes of two integers within a list that added up to some target value.

## Approach
My first thought was immediately to enumerate the list so I would have easy access to both the value and index of each item. From there, I first made a nested loop that would run through every possible combination of two items in the list and check if they added up to the target. However, this was quite inefficient, as the time taken to compute the result would scale at a rate proportional to the square of the number of items in the list. 

As a result, I pivoted to trying to find ways to reduce the number of computations. I first tried to sort the list in ascending order and only check the numbers which were less than half of the target, but I quickly realized that this would also be of the order n^2. 

My next thought was to make some kind of converter between the value and index of a number in the list, updating it as I ran through all the items in the list. I settled on a dictionary and replaced the nested loop with a quick check to see if any of the keys in the dictionary was equal to the target - the current value I was checking (ie. dict key + current value == target). This allowed me to get a code with a linear time complexity. 

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n):
    Although the first iteration of my code had O(1) space complexity, I had to sacrifice it to decrease my time complexity by adding a dictionary. 

## Edge Cases / Notes

## Reflections
<What you learned, mistakes made, alternative approaches>
One thing I realized was that checking if an item is in a dictionary or some other iterable doesn't have a linear time complexity, as the operation doesn't run through all of the items in the iterable. This is especially important, as using an iterable in this way can drastically reduce the time complexity of my code. 