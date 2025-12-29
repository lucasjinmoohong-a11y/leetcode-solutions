"""
Approach:
I made it so that the value being added to the "total" would be popped from the "nums" list immediately
after being taken to ensure the "x" value is accurate. I also ensured that k was being updated each 
iteration so that the values don't default to the maximum.

Time Complexity:  O(n^3)
Space Complexity: O(n)

Issues:
Outputs correct values, but very inefficient due to cubic time complexity. 
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
                    k-=(current-x)*self.factorial(current-1)
                    nums.pop(current-x)
                    break
            current-=1
        
        return str(total)


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
