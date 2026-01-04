"""
Approach:
I created a helper function that would run through all root-leaf paths and return True if one worked.
I did this through recursion; the root would be added to a 'sum' variable, which was compared to the
targetSum; if they were equal and it was a leaf node, the function would return True. Otherwise: it
would return False. It would then try running the function on the root's children; if both were False, 
the function would return False. Otherwise: it would return True. 

Time Complexity:  O(n)
Space Complexity: O(log(n))

Issues:
Doesn't work with negative elements

Tests:
[-2, null, -3], -5 --> False, expected: True
"""

class Solution(object):
    def helper(self, sum, root, targetSum):
        if not root:
            return False
        
        sum += root.val
        
        if sum > targetSum:
            return False

        if not root.left and not root.right:
            if sum == targetSum:
                return True
            else:
                return False

        if self.helper(sum, root.left, targetSum):
            return True
        if self.helper(sum, root.right, targetSum):
            return True

        return False

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        sum = 0
        return self.helper(sum, root, targetSum)


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
