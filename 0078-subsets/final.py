"""
Approach:
I added ordering to my subsets by adding another conditional to the adding of a new element to a 
subset; the new element would have to be greater than the last element of the subset. Because the code
is recursive, this means that it would have to be the max element of the list, and the list would be
ordered in ascending fashion. This took away all duplicates.

Time Complexity:  O(n*2^n)
Space Complexity: O(n*2^n)

Tests:
[1,2,3] --> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
[0] --> [[],[0]]
"""

class Solution(object):
    def helper(self, rlist, subset, nums):
        for num in nums:
            temp = subset[:]
            if not temp or num not in temp and num > temp[-1]:
                temp.append(num)
                rlist.append(temp)
                self.helper(rlist, temp, nums)
            

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rlist = []
        self.helper(rlist, [], nums)
        rlist.append([])
        return rlist


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))

