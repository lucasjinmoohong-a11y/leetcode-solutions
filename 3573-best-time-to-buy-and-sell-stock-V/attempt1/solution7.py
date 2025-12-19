"""
Approach:
I added logic that compares the two possible trades for any given critical point and uses that 
information to choose between making the transaction at the critical point, or one day before
that critical point.

Issues:
The problem is that the code doesn't allow for choosing between different starting transactions. 
For example, in the second test below, the code makes a transaction on the first day, which disallows
it from trying a transaction on the second day, which would give the single largest progit margin. 

Tests:
[12,16,19,19,8,1,19,13,9], 3 --> 36 (7,11,18) --> correct
[14,6,10,19], 1 --> 9, correct answer: 13
"""

def findCrit(list, val, ind):
    #print(f"NEW TRANSACTION: day {ind}")
    crit = 0
    days_passed = 0
    #print((val, ind))
    for next_index, next_value in enumerate(list):
        #print((next_index, next_value))
        #print(crit)
        if next_index > ind:
            temp = next_value-val
            #print(temp)
            if (temp <= crit and crit > 0) or (temp >= crit and crit < 0): 
                break
            else: 
                crit = temp
                days_passed += 1
    
    if ind+days_passed != len(list)-1:
        if list[ind+days_passed+1] >= list[ind+days_passed-1] and crit > 0 or list[ind+days_passed+1] <= list[ind+days_passed-1] and crit < 0:
            return (abs(crit), ind+days_passed)
        else: 
            return (abs(list[ind+days_passed-1]-val), ind+days_passed-1)
    else: 
        return (abs(crit), ind+days_passed)

class Solution(object):
    def maximumProfit(self, prices, k):
        isTransactionRunning = False
        transactionsDone = []
        total = 0
        nextday = 0

        for today_index, today_value in enumerate(prices):
            if isTransactionRunning == False:
                isTransactionRunning = True
                store = findCrit(prices, today_value, today_index)
                nextday = store[1]
                transactionsDone.append(store[0])
            if today_index == nextday:
                isTransactionRunning = False
        
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
    print(sol.maximumProfit([12,16,19,19,8,1,19,13,9], 3))

