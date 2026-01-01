"""
Approach:
Added edge-case: if the current node doesn't exist, the function simply returns the root.

Issues:
Code keeps returning the exact same BST

Tests:
[5,3,6,2,4,null,7], 3 --> [5,3,6,2,4,null,7], correct answer: [5,4,6,2,null,null,7]
[5,4,6,2,null,null,7], 0 --> [5,4,6,2,null,null,7]
[], 0 --> []
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
            curr = self.minRight(curr)
        
        return root
        


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
