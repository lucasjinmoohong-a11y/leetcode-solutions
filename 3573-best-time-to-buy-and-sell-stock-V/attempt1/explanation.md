# Problem: 3573. Best Time to Buy and Sell Stocks V

## Problem Summary
Given a list for a certain stock that tracks the price on a certain day, use the information to either buy or short a stock. Given that you can make a maximum of k transactions, that you can have a maximum of one transaction running at any given time, and that you cannot start a new transaction on the same day you ended another, what is the maximum amount of money you can earn. 

## Approach
My first approach was to create a function that would find the biggest deviation in prices for any given data point within the prices list. From there, I could compare the transactions and take the k largest transactions. This approach was quite flawed, however, as it didn't take into account the restriction that only one transation could be running at any given time. 

My second approach was inspired by the given LeetCode hints; I created a variable that would track whenever a transaction was running, which would ensure that I met the 'max of one transaction at any given time' restriction. Moreover, instead of finding the maximum deviation in sales prices, I decided on a method that would find turning points in the prices list (when the prices go from increasing to decreasing, or vice versa), taking those points instead. 

However, this approach was also flawed. For one, it failed to take into account the fact that the best transaction could go past a turning point, especially in cases where k is proportionally far smaller compared to n (the length of the list prices).

Ultimately, I wasn't able to solve the problem. I will come back later and make another attempt. 

## Complexity Analysis
- Time Complexity:  O(n^2)
- Space Complexity: O(n)
--> n is the length of prices

## Reflections
I realized that sometimes approaches are fundamentally flawed, and those flaws cannot simply be fixed by saavy programming. Rather than come up with a basic idea and trying to code it immediately, it is often better to take more time absorbing the problem and coming up with a more elegant solution. 