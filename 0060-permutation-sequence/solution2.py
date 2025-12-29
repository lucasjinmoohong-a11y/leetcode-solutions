"""
Approach:
When finding the first digit of the output, I used the nums list rather than taking the value directly 
using n. From there, I popped the taken value from the nums list to prevent double-counting. 

Time Complexity:  O()
Space Complexity: O(...)

Issues:


Tests:
<inputs> --> <outputs>, <does it work?>
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
                total+=nums[n-x]*pow(10,n-1)
                break
        nums.pop(n-x)
        
        return str(total)

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.getPermutation(3,1))
