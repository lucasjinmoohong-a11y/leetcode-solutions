"""
Approach:
I tried to make a recursive function, because I realized that the process of building a treewould be 
the same whether it was the full tree or a subtree; all that had to be changed was the preorder/inorder
lists. I first tried to only change the preorder list. I partitioned the preorder lists about the root 
node and recursively called the function again for the left and right children of the root. Finally, 
the code would return the current node. 

Issues:
Listed below

Test1:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
output = [3,9,null,20,null,15,null,7]
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
    def subTree(self, preorder, inorder):
        if not preorder:
            return
        curr = TreeNode(preorder.pop(0))

        # partition logic doesn't work: 
        temp = []
        lsub = []
        rsub = []
        
        for n in inorder: # should stop after finding the root, but doesn't --> all this does is delete 
            # root from temp 
            if n != curr.val:
                temp.append(n)

        for n in preorder: # fails because temp is wrong
            if n in temp:
                lsub.append(n)
            else:
                rsub.append(n)
        
        curr.left = self.subTree(lsub, inorder) # should include a modified inorder; keeping inorder 
        # the same will likely lead to problems in partitioning

        curr.right = self.subTree(rsub, inorder) # should include a modified inorder; keeping inorder 
        # the same will likely lead to problems in partitioning

        return curr

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        root = self.subTree(preorder, inorder) # not necessary; can just return the function

        return root # if just return the function, then no need to create a separate recursive function


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))




        