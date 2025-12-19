"""
Approach:
I flipped the value and index in enumerate (line x), which was causing me a lot of problems. I also
fixed the day logic, as the previous logic allowed transactions to be made on the same day one ended.

Issues:
The findCrit function seems to be flawed in that it takes the last maximum deviation from the original
value instead of the first.

Tests:
[1,7,9,8,2], 2 --> 14 (8,6) --> correct
[12,16,19,19,8,1,19,13,9], 3 --> 11 (7,4), correct answer: 36 (7,11,18)

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

