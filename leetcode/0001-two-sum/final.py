"""
Approach:
Store values and indexes of each integer in a dictionary that is updated as I run through all integers 
in the list, checking whether there exists a number in the dictionary that can sum to the target value.

Time Complexity:  O(n)
Space Complexity: O(n)

Tests: 
([2,7,11,15], 9) --> [0,1], it works
"""

class Solution:
    def twoSum(self, nums, target):
        value_to_index = {}
        for index, value in enumerate(nums):
            newtarget = target-value
            if newtarget in value_to_index:
                return [value_to_index[newtarget], index]
            value_to_index[value] = index
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
