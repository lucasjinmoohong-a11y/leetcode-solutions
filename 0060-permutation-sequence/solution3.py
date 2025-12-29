"""
Approach:
I added a "current" variable which would track the number of times the previous code would run. Using
this variable, I could put the code in a while loop and allow it to keep running for each digit of 
the output. 

Time Complexity:  O(n^3)
Space Complexity: O(n)

Issues:
The output is completely wrong for subsequent digits, with only the first digit being correct. Many 
digits are used multiple times, which should be impossible. 

Tests:
(3,3) --> 233, correct answer: 213
(4,9) --> 2444, correct answer: 2314
(3,1) --> 111, correct answer: 123
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
        
        current = n
        total = 0

        while current > 0:
            for x in range(1, current+1): 
                if k > (current-x)*self.factorial(current-1):
                    total+=nums[current-x]*pow(10,current-1)
                    break
            current-=1
            nums.pop(current-x)
        
        return str(total)

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.getPermutation(4,9))
