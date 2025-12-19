"""
Approach:
I flipped the system that ensured that each day wasn't being used twice in transactions; all indexes 
would be considered in the maxOfList function at the beginning, but they would be disallowed from
being considered again if they were used in a transaction.

Issues:
Although the system disallows starting multiple transactions on the same day, it does not consider
the fact that you cannot make a transaction on the same day you ended it.

Tests:
[1,7,9,8,2], 2 --> 15 (8,7), correct answer: 14
[12,16,19,19,8,1,19,13,9], 3 --> 54 (18,18,18), correct answer: 36
"""

def maxOfList(list, val, ind):
    templist = []
    for index, value in enumerate(list):
        if index not in ind:
            templist.append(abs(value-val))
    return max(templist)

def minimum(list):
    if list:
        return min(list)
    else: 
        return 0

class Solution(object):
    def maximumProfit(self, prices, k):
        best_k = []
        indexes = [int in range(len(prices))]

        total = 0
        
        for index, value in enumerate(prices):
            if maxOfList(prices, value, indexes) > minimum(best_k) or len(best_k) < k:
                best_k.append(maxOfList(prices, value, indexes))
                indexes.append(index)
            
            if len(best_k) > k:
                best_k.remove(minimum(best_k))

        for item in best_k:
            total += item
        print(total)
        print(best_k)
            
            

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    sol.maximumProfit()

