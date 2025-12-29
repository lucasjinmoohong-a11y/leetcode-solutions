"""
Approach:
Fixed the index mismatch; instead of finding the index within the list, which will sometimes get the 
wrong value because the index function takes the first instance of the value, I decided to enumerate 
the list. 

Time Complexity:  O(n)
Space Complexity: O(n)

Tests:
-32767 --> -76723
"""

class Solution:
    def reverse(self, x):
        list = []
        for i in str(abs(x)):
            list.append(int(i))
        
        total = 0
        
        for index, value in enumerate(list):
            total += value*pow(10,index)

        if total > pow(2,31)-1:
            total = 0

        if x >= 0: 
            return total
        else: 
            return -total


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
