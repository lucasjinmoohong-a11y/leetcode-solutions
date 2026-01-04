"""
Approach:
I removed the "if sum > targetSum: return False" because this would only work for non-negative 
elements.

Time Complexity:  O(n)
Space Complexity: O(log(n))

Tests:
[-2, null, -3], -5 --> True
"""

class Solution(object):
    def helper(self, sum, root, targetSum):
        if not root:
            return False
        
        sum += root.val

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
