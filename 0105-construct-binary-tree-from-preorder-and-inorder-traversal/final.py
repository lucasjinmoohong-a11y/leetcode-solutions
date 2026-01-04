"""
Approach:
I first fixed the partition logic using slicing. I found the index of the root node within inorder and
used it to partition the inorder list into the right and left subtree's inorder list. Next, I 
partitioned the preorder list by making the left subtree's preorder list the first idx-1 elements after 
the root node, and then leaving the rest as the right subtree's preorder list. I then got rid of the
subtree function because it was unnecessary and could have just been put in the buildTree() function.

Time Complexity:  O(n^2)
Space Complexity: O(n^2)

Test1:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
output = [3,9,20,null,null,15,7]
expected = [3,9,20,null,null,15,7]

Test2:
preorder = [-1]
inorder = [-1]
output = [-1]
expected = [-1]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return
        curr = TreeNode(preorder[0])
        
        idx = inorder.index(curr.val)

        lsub_in = inorder[:idx]
        rsub_in = inorder[idx + 1:]

        lsub_pre = preorder[1:1 + len(lsub_in)]
        rsub_pre = preorder[1 + len(lsub_in):]
        
        curr.left = self.buildTree(lsub_pre, lsub_in)

        curr.right = self.buildTree(rsub_pre, rsub_in)

        return curr
    

if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
