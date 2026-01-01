"""
Approach:
Let curr = root. While curr exists, iterate through the binary tree, going left when curr > val and 
right when curr < val. After the final iteration, curr will be Null; using the previous node of curr,
compare prev to val and place the leaf node accordingly. 

Time Complexity:  O(log(n))
Space Complexity: O(1)

Issues:
Doesn't work when the root doesn't exist.

Tests:
[], 5 --> error: local variable 'prev' referenced before assignment
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
