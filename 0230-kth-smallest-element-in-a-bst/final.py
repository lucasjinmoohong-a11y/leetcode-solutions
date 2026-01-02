"""
Approach:
Run through the BST with an inorder traversal, appending values to a list as encountered. Finally, 
return the (k-1) indexed element in the list (because elements in BST are 1-indexed). 

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return
        self.inorderTraversal(root.left)
        rlist.append(root.val)
        self.inorderTraversal(root.right)


    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        global rlist
        rlist = []
        self.inorderTraversal(root)
        return rlist[k-1]


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
