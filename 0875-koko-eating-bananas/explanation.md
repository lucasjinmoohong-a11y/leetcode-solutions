# Problem: 875. Koko Eating Bananas

## Problem Summary
There is a list 'piles,' where piles[i] represents the number of bananas in the i-th pile of bananas. Each hour, Koko (a monkey) chooses a pile of bananas and eats k bananas from it; if k > piles[i], then Koko eats the whole pile and waits until the next hour to eat from another pile. Find the minimum k such that Koko eats all the bananas within h hours. 

## Approach
I first created a function that would determine whether an eating speed of k bananas per hour could work. The canEat() function added up all of the bananas in the 'piles' list, rounding up to the nearest multiple of k for each pile, and checked whether that sum was equal to or less than k * h (Koko's max number of bananas eaten in h hours). If it was equal to or less than k * h, canEat() returns True; otherwise, it returns False. 

Next, I simply created a binary search algorithm. I set pointers at 1 banana per hour and max(piles) bananas per hour, because 0 bananas per hour would never work and anything greater than max(piles) bananas per hour would work just as well as max(piles) bananas per hour. From there, the binary search algorithm would track the smallest k thus far, before returning k when the pointers crossed (left > right). 

## Complexity Analysis
- Time Complexity: O(nlog(M)), n = number of piles, M = max(piles)
- Space Complexity: O(1)