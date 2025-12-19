"""
Approach:
First, I changed < to <= in findCrit to decrease time spent on each transaction. This would ensure that
if the value following a critical point is identical to the critical point, it will choose the 
critical point rather than wait. 

I also changed the logic so that the function would check whether crit is pos/neg, rather than
checking whether temp is pos/neg. This would fix some of the errors, temp changes at the beginning of 
each iteration, while crit only changes after each iteration.

Issues:
The problem is that checking for crit numbers does not work bc you cannot make 2 trades in same day. 
In the case where the next critical point could be used in another transaction, one must compare 
both possible trades. For example, in the second test below, one would have to compare the following:
12-19, 19-1, 19-9 VS 12-19, 19-8, 1-19

Tests:
[1,7,9,8,2], 2 --> 14 (8,6) --> correct
After change 1: [12,16,19,19,8,1,19,13,9], 3 --> 17 (7,10), correct answer: 36 (7,11,18)
After Change 2: [12,16,19,19,8,1,19,13,9], 3 --> 35 (7,18,10), correct answer: 36 (7,11,18)
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
            if (temp <= crit and crit > 0) or (temp >= crit and crit < 0): 
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

        for today_index, today_value in enumerate(prices):
            if isTransactionRunning == False:
                isTransactionRunning = True
                nextday = findCrit(prices, today_value, today_index)[1]
                transactionsDone.append(findCrit(list=prices, val=today_value, ind=today_index)[0])
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

