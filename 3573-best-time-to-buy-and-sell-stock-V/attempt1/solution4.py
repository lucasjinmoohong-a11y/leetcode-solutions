"""
Approach:
I looked at the given leetcode hints:
1. Use dynamic programming.
2. Keep the following states: idx, transactionsDone, transactionType, isTransactionRunning.
3. Transactions transition from completed -> running and from running -> completed.

I also realized that transactions should only occur at turning points if you look at the list of 
numbers as a graph. 

Using this, I created a function called findCrit() that would intake a data point in the prices list.
From there, it would run through all of the following data points, keeping track of whether it is
increasing or decreasing. The moment it changes directions, the function logs the data point by
returning its 'distance' to the original value (the amount of money gained in a transaction) and its 
index as a tuple.

In the solution, I keep track of the isSolutionRunning state to ensure new transactions are only made
when a transaction is not currently running. On days when no transaction is running, I run the 
findCrit function and keep track of the best transaction using the transactionsDone list. I only keep 
the best k transactions, before finally returning their sum. 

Time Complexity:  O(n^2)
Space Complexity: O(n)

Issues:
<problems to fix, challenges I am facing>

Tests:
[1,7,9,8,2], 2 --> 11 (9,2)
"""

def findCrit(list, val, ind):
    crit = 0
    days_passed = 0
    #print((val, ind))
    for next_index, next_value in enumerate(list):
        #print((next_index, next_value))
        #print(crit)
        if next_index > ind:
            temp = next_value-val
            #print(temp)
            if temp < crit and temp > 0 or temp > crit and temp < 0: 
                break
            else: 
                crit = temp
                days_passed += 1

    #print(crit)
    #print(days_passed)
    return (abs(crit), ind+days_passed)

class Solution(object):
    def maximumProfit(self, prices, k):
        isTransactionRunning = False
        transactionsDone = []
        total = 0
        nextday = 0

        for today_value, today_index in enumerate(prices):
            if isTransactionRunning == False or today_index == nextday:
                isTransactionRunning = True
                nextday = findCrit(prices, today_value, today_index)[1]
                transactionsDone.append(findCrit(list=prices, val=today_value, ind=today_index)[0])
        
        while len(transactionsDone) > k:
            transactionsDone.remove(min(transactionsDone))
        
        for transaction in transactionsDone:
            total += transaction

        #print(transactionsDone)
        #print(total)
        return total
                


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.maximumProfit([1,7,9,8,2], 2))

