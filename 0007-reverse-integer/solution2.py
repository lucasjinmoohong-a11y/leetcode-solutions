"""
Approach:
Added in edge case when x is greater than 32-bit. 

Time Complexity:  O(n^2)
Space Complexity: O(n)

Issues:
Does not work in certain cases. 

Tests:
-32767 --> -7423, proper answer: -76723
"""

class Solution(object):
    def reverse(self, x):
        list = []

        for i in str(abs(x)):
            list.append(int(i))
        
        total = 0
        
        for n in list:
            total += n*pow(10,list.index(n))
        
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
