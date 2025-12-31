"""
Approach:
<your strategy for solving it>

Time Complexity:  O(...)
Space Complexity: O(...)

Issues:
<problems to fix, challenges I am facing>

Tests:
<inputs> --> <outputs>, <does it work?>
"""

class Solution(object):
    def canEat(self, piles, k, h):
        total = 0
        for x in piles:
            total += (x + k - 1) // k * k
        if total > k*h:
            return False
        else:
            return True


    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        min = 0

        while left <= right:
            middle = (left + right) // 2
            if self.canEat(piles, middle, h):
                min = middle
                right = middle - 1
            else:
                left = middle + 1
        return min

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
