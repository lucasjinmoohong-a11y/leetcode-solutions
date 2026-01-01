"""
Approach:
I fixed the problem when the root doesn't exist by adding an edge-case to the beginning of the solution;
if the root doesn't exist, the code returns a new TreeNode with the given value. 

Time Complexity:  O(log(n))
Space Complexity: O(1)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root: 
            return TreeNode(val)

        curr = root
        while curr:
            prev = curr
            if curr.val > val:
                curr = curr.left

            elif curr.val < val:
                curr = curr.right
            
        if prev.val > val:
            prev.left = TreeNode(val)
        elif prev.val < val:
            prev.right = TreeNode(val)

        return root


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
