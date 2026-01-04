"""
Approach:
My first thought was to create a helper function that would recursively create new subsets and append
them to the return list. I appended None to nums to account for the case in which a subset would end
without adding another element. From there, I ran a function that would intake a subset and check
if its last element was None. If it was, it would be appended to the return list without the None. 
Otherwise, every element in nums would be appended to it, as long as it was not already in the subset.

Issues:
First, there would only be a maximum of len(nums) items in the return list because the outer loop
that would call the helper function was bounded by the number of elements in nums. 
Second, appending the subset simply didn't work in the code, as it just became null. 

Tests:
[1,2,3] --> [[null],[null],[null],[null], expected:[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
[0] --> [[null],[null]], expected:[[],[0]]
"""

class Solution(object):
    def helper(self, subset, nums):
        if not subset[-1]:
            return subset.pop()
        else:
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    return self.helper(subset, nums)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rlist = []
        nums.append(None)
        for num in nums:
            rlist.append([self.helper([num], nums)])
        return rlist


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
