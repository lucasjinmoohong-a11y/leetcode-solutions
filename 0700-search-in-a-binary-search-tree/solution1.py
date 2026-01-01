"""
Approach:
I created a recursive function that checks whether or not the target value == the current Node's value.
If it is, then it returns the node; if the target is larger, it goes to the Node's right child; if it 
is smaller, it goes to the Node's left child. It runs the function on the new node; if the node doesn't
exist, then it returns None because the target value is not in the tree. 

Time Complexity:  O(log(n))
Space Complexity: O(1)

Issues:
Always returns none.

Tests:
[4,2,7,1,3], 2 --> None, correct answer: [2,1,3]
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
                self.searchBST(root.left, val)
            elif root.val < val:
                self.searchBST(root.right, val)
            else:
                return root
        else:
            return None
        

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
