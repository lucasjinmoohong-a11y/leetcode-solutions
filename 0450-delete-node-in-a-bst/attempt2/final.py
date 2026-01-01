"""
Approach:
If the root DNE, then return the root. Otherwise, if the value of the root > key, then set root.left
to deleteNode(root.left, key) to rerun the function. If root.val < key, do the same for root.right. 
If they are equal, there are four cases. First, if neither root.left or root.right exist, then return
None (meaning that the pointer pointing to the node now points to None). If only one exists, then
return it (meaning the pointer now points to the remaining child and skips the current node). If both
exist, then find the smallest node greater than the current node and replace the current node with it.
Then, call the function again on the right subtree (so that you delete the other copy of the value
you replace the key with). Finally, return root. 

Time Complexity:  O(h)
Space Complexity: O(h)
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
            return root
        
        if root.val > key: 
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right

            elif not root.right:
                return root.left
            else:
                min = self.minRight(root)
                root.val = min.val
                root.right = self.deleteNode(root.right, min.val)
        return root


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
