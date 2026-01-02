"""
Approach:
I created a recursively called function inorder() that would run the root's left child first (because 
it is less than the root), then the root itself, and then the root's right child. Because it is called
recusively, it will run the node furthest left first and go in-order from there. To track these values,
I created an empty list rlist that would be appended to during inorder(). Finally, rlsit was returned.

Time Complexity:  O(N)
Space Complexity: O(N)
"""

class Solution(object):
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        rlist.append(root.val)
        self.inorder(root.right)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        global rlist 
        rlist = []
        self.inorder(root) 
        return rlist


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
