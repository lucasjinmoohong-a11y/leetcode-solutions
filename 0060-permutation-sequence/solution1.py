"""
Approach:
I set up a factorial function, as the math module is not supported in LeetCode. I then created a "nums"
list, which stores the digits 1 to n. Finally, I noticed that when k > (n-1)*(n-1)!, the first
digit of the output is n. Moreover, when k > (n-2)*(n-1)!, the first digit is n-1, and so on. From
there, I created a for loop that would find the smallest x such that k > (n-x)*(n-1)!, which could be 
used to find the first digit of the output. 

Time Complexity:  O(n^2)
Space Complexity: O(n)

Issues:
However, this only works for the very first digit of the output. 

Tests:
(3,3) --> 200, correct answer: 213
(4,9) --> 2000, correct answer: 2314 
(3,1) --> 100, correct answer: 123

--> achieves goal of the basic code but needs to be iterated in order to be a solution.
"""

class Solution(object):
    def factorial(self, n):
        total = 1
        for i in range(1,n+1):
            total=total*i
        return total
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = []
        for num in range(1, n+1):
            nums.append(num)
        
        total = 0

        for x in range(1, n+1): 
            if k > (n-x)*self.factorial(n-1):
                total+=(n-x+1)*pow(10,n-1)
                break
        
        return str(total)

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.getPermutation(3,1))
