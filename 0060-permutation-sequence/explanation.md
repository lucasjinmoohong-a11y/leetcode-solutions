# Problem: 60. Permutation Sequence

## Problem Summary
Given a list of integers from 1 to n, there are n! permutations of the list. If these permutations are sorted in ascending order, return the k-th permutation sequence in string form.

## Approach
I first set up the backbone of my solution, such as a factorial function and a "nums" list that stores the digits 1 to n. Next, I noticed that when k > (n-1)*(n-1)!, the first digit of the output is n. 
Moreover, when k > (n-2)*(n-1)!, the first digit is n-1, and so on. From there, I created for loop that
would find the smallest x such that k > (n-x)*(n-1)!, which could be used to find the first digit of the output. 

I next tried to expand this into an iterable function. My second iteration included a system that used the nums list to find the first digit of the output instead of taking the value directly using n. This allowed me to change the subsequent values available to be the next digit of the output, as I then popped the taken value from the nums list to prevent double-counting. 

In my third iteration, I added a "current" variable which would track the number of times the previous code would run. Using this variable, I could put the code in a while loop and allow it to keep running for each digit of the output. However, the output was completely wrong for subsequent digits, with only the first digit being correct. Furthermore, many digits were used multiple times, which should have been impossible. 

Finally, I made it so that the value being added to the "total" would be popped from the "nums" list immediately after being taken to ensure the "x" value is accurate. I also ensured that k was being updated each iteration so that the values don't default to the maximum. This fixed the issues and ensured proper outputs each time.

## Complexity Analysis
- Time Complexity:  O(n^3) - extremely inefficient, but n ranges from 1 to 9, so a high time complexity is relatively okay.
- Space Complexity: O(n)

## Reflections
I learned that taking a step back and finding an initial pattern is extremely important in coding. Without realizing the pattern of the first digit in my first iteration, I would have never been able to extrapolate the method using a while loop. Ultimately, patterns are the backbone of coding, and should be prioritized over immediately jumping into writing a solution. 