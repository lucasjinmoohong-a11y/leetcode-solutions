"""
Approach:
I first created a dfs function that would take in an array and its sum. If the sum is equal to the 
target value, it is appended to the return list. Otherwise, the function runs through all the values
in the candidates list: if it is less than or equal to the target-sum (meaning adding it to the sum
will be less than or equal to the target) and it is greater than or equal to the last element of the
temporary list (meaning that the list is sorted in ascending order and duplicate arrays aren't 
returned). Finally, I call the function with the initial parameters [] and 0, and then return the 
rlist.

Time Complexity:  O(n^(t/m)), n = number of candidates, t = target value, m = minimum candidate value
Space Complexity: O(t/m)
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rlist = []

        def dfs(curr, sum):
            if sum == target:
                rlist.append(curr)
            else:
                for i in candidates:
                    temp = curr[:]
                    if not temp or i <= target - sum and i >= temp[-1]:
                        temp.append(i)
                        dfs(temp, sum+i)
        dfs([],0)
        return rlist


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))


