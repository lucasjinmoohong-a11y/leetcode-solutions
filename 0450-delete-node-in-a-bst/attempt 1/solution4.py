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
            prev = curr
            if curr.val > key:
                curr = curr.left
            elif curr.val < key:
                curr = curr.right
        
        if not curr:
            return root

        if curr.left == None and curr.right == None:
            if prev.val > curr.val: 
                prev.left = None
            else:
                prev.right = None

        elif curr.left == None:
            curr.val = curr.right.val
            curr.right = self.deleteNode(curr.right, curr.right.val)

        elif curr.right == None:
            curr = curr.left
            curr.left = self.deleteNode(curr.left, curr.left.val)
        else:
            x = self.minRight(curr)
            curr.val = x.val
            self.deleteNode(curr.right, x.val)
        
        return root
        


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
