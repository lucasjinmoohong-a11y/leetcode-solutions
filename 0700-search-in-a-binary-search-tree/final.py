"""
Approach:
I fixed the recursive logic by adding 'return.'

Time Complexity:  O(log(n))
Space Complexity: O(1)

Tests:
[4,2,7,1,3], 2 --> [2,1,3]
[4,2,7,1,3], 5 --> None
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root:
            if root.val > val:
                return self.searchBST(root.left, val)
            elif root.val < val:
                return self.searchBST(root.right, val)
            else:
                return root
        else:
            return None
        

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
