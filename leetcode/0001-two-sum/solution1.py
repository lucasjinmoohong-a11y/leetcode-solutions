"""
LeetCode Problem: <problem-number> - <problem-title>

Description:
<short description of the problem>

Approach:
<your strategy for solving it>

Time Complexity:  O(...)
Space Complexity: O(...)
"""

class Solution:
    def twoSum(self, nums, target):
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if value1+value2 == target:
                    return [index1, index2]
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
