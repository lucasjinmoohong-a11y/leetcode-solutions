"""
Approach:
Create a function (maxOfList) that takes in a list and a data point within that list. The function will 
split out the largest deviation between the given data point and any other data point within the list. 

From there, enumerate the values within the list; as long as the data point hasn't already been
used in a previous transaction, take the maxOfList of that data point and add it to a best_k list, 
which tracks all transactions. Only keep track of the highest transactions within best_k, and return
the sum of the best k transactions. 

Time Complexity:  O(n^3)
Space Complexity: O(n+k)
--> n: # of elements in prices
--> k: max # of transactions

Issues:
The most immediate issue is that min() doesn't work for empty lists.
"""

def maxOfList(list, val, ind):
    templist = []
    for index, value in enumerate(list):
        if index in ind:
            templist.append(abs(value-val))
    return max(templist)

class Solution(object):
    def maximumProfit(self, prices, k):
        best_k = []
        indexes = []
        total = 0
        
        for index, value in enumerate(prices):
            indexes.append(index)
            
            if maxOfList(prices, value, indexes) > min(best_k) or len(best_k) < k:
                best_k.append(maxOfList(prices, value, indexes))
                indexes.remove(index)
            
            if len(best_k) > k:
                best_k.remove(min(best_k))

        for item in best_k:
            total += best_k
        return total
            
            

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
