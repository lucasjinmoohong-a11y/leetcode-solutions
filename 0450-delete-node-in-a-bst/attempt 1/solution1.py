"""
Approach:
If the root DNE, return None. Otherwise, search for the key value. When found: if the node has 0 child
nodes, set the node to None. If the node has 1 child node, set the node to the existing child node. 
If the node has 2 children nodes, set the node to the smallest node in the right subtree of the node 
(the smallest node greater than the node).

Issues:
Code does not run.

Tests:
line 40: 'NoneType' object has no attribute 'val' 
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minRight(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        curr = root
        while curr.val != key:
            if curr.val > key:
                curr = curr.left
            elif curr.val < key:
                curr = curr.right

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
