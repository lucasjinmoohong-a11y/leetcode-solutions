"""
Approach:
I first reworked my code to include the appending of the subset to the return list within the recursive
function, rather than in the main code. This would ensure that the number of subsets wouldn't be
bounded by the number of elements in nums. Next, I included the case of the empty list at the end of
my code, instead opting to include the case where subsets stop adding new elements in the helper
function. Finally, I created a temporary copy of the subset between each adding of a new element
to the subset. This would ensure that not all elements would be added to a subset at once.

Issues:
The code repeats elements multiple times; instead of each combination of x elements, it takes each 
permutation of them.

Tests:
[1,2,3] --> [[1],[1,2],[1,2,3],[1,3],[1,3,2],[2],[2,1],[2,1,3],[2,3],[2,3,1],[3],[3,1],[3,1,2],[3,2],
[3,2,1],[]], expected:[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

[0] --> [[],[0]]
"""

class Solution(object):
    def helper(self, rlist, subset, nums):
        for num in nums:
            temp = subset[:]
            if num not in temp:
                temp.append(num) 
                rlist.append(temp) # now here, instead of in main code
                self.helper(rlist, temp, nums)
            

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rlist = []
        self.helper(rlist, [], nums)
        rlist.append([]) # include null case
        return rlist


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))

