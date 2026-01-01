"""
Approach:
Added logic where, if the current node has 2 children, it will replace the current node's value to 
that of the smallest node larger than it and rerun deletNode() on said node. 

Issues:
Code doesn't run.

Tests:
error: maximum recursion depth exceeded in cmp
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minRight(self, node):
        x = node.right
        while x.left:
            x = x.left
        return x

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        
        curr = root
        while curr and curr.val != key:
            if curr.val > key:
                curr = curr.left
            elif curr.val < key:
                curr = curr.right
        
        if not curr:
            return root

        if curr.left == None:
            curr = curr.right
        elif curr.right == None:
            curr = curr.left
        else:
            x = self.minRight(curr)
            curr.val = x.val
            curr.right = self.deleteNode(curr, x.val)
        
        return root
        


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
