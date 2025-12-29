"""
Approach:
Convert the integer into an unsigned list. From there, add each value in the list to a variable, total, 
while keeping in mind the place value of each value in the list so that total will be in reverse of x. 
Use x to find the sign of the output and return the corresponding total. 

Time Complexity:  O(n^2)
Space Complexity: O(n)

Issues:
Forgot to implement case when input is greater than 32-bit; should return 0.

Tests:
1534236469 --> 9012028651, correct answer: 0
"""

class Solution(object):
    def reverse(self, x):
        list = []

        for i in str(abs(x)):
            list.append(int(i))

        total = 0

        for i in list:
            total += i*pow(10,list.index(i))

        if x >= 0: 
            return total
        else: 
            return -total


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
