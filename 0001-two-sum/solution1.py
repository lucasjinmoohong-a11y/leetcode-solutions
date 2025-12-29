"""
Approach:
Nested loop to run through each combination of pairs within the list(nums)

Time Complexity:  O(n^2)
Space Complexity: O(1)

Issues:
Time complexity is too high; quadratic time complexity would make computations very difficult for 
larger inputs.

Tests: 
([2,7,11,15], 9) --> [0,1], it works
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
