# Problem: 12. Integer to Roman

## Problem Summary
Create a function that converts an integer into its roman numeral expression. Inputs are between 1 and 3999, inclusive.

## Approach
I first decided to create a dictionary for each roman numeral, using its corresponding integer value as the key because the function must convert an integer into its roman numeral counterpart. 

From there, I decided to convert the string into a list, as it would allow me to retrieve individual place values of the integer at a time. 

Next, I set up an output string that I would add onto as I moved through the place values of the integer. 

In order to keep track of the place value(index) and value of each place value of the integer, I enumerated the list. I then set up the additive and subtractive logic for each place value: 
1. If the value is 0-3, then write out *value* "I"s (adjust the roman numeral based on the place value of the number. ex: "X" for tens place) 
2. If the value is 4-5, then write out *5-value* "I"s and then a "V" (adjust again if necessary)
3. If the value is 6-8, then write out a "V" and then follow the logic from condition 1 (achieved by subtracting the value by 5 and putting all the subtractive logic in a while loop)
4. If the value is 9, then write out an "I" and then an "X" (adjust again: value is 10x more than the place value)

Finally, I returned the output string. 

## Complexity Analysis
- Time Complexity: O(log(n))
- Space Complexity: O(log(n))
--> the code scales by the number of digits in the base-10 input, or the log(n)

## Reflections
I learned to never title variables by a python keyword; my first iteration had the input variable (now named 'num') as 'input,' which led to the list storing the digits of the input being messed up. It was an easy fix, as I simply renamed it num, however it reminded me of the importance of having good coding habits and double checking my work. 