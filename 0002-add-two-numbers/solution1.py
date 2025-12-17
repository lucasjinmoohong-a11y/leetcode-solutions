"""
Approach:
For each number in each list, add its value multiplied by its place value (10^index) to an output 
integer. Then, split the output string into a list, reverse the list's order, and then return it. 

Time Complexity:  O(n)
Space Complexity: O(n)

Issues:
First, although the code works and returns the correct result, it does not return it in the correct 
format (a linked list). 

Second, the len function does not work in Leetcode, because the input to the function is also a linked 
list. 

Tests:
[2,4,3], [5,6,4] --> [7,0,8], incorrect format (list instead of linked list)
"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Write your code here
        output = 0
        for n in range(len(l1)-1, -1, -1):
            output+=l1[n]*pow(10, n)
        for n in range(len(l2)-1, -1, -1):
            output+=l2[n]*pow(10, n)

        output = str(output)
        new = []
        for item in output:
            new.append(int(item))
        new.reverse()
        return new


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.addTwoNumbers([2,4,3], [5,6,4]))

