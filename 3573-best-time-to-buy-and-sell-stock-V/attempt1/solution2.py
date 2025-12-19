"""
Approach:
I fixed the issue of min() not working for empty lists by creating my own function (minimum()) that 
functions identically to min(), but returns 0 if the input list is empty. 

Issues:
The maxOfList function doesn't give correct outputs, because it doesn't account for values that occur 
later on (ones that have not yet been enumerated through). 

Tests:
[1,7,9,8,2], 2 --> 8, correct answer: 14
[12,16,19,19,8,1,19,13,9], 3 --> 39, correct answer: 36
"""

def maxOfList(list, val, ind):
    templist = []
    for index, value in enumerate(list):
        if index in ind:
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
        indexes = []
        total = 0
        
        for index, value in enumerate(prices):
            indexes.append(index)
            
            if maxOfList(prices, value, indexes) > minimum(best_k) or len(best_k) < k:
                best_k.append(maxOfList(prices, value, indexes))
                indexes.remove(index)
            
            if len(best_k) > k:
                best_k.remove(minimum(best_k))

        for item in best_k:
            total += item
        return total
            
            

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    sol.maximumProfit([1,7,9,8,2], 2)

