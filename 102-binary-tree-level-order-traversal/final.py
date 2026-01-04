"""
Approach:
I implemented a BFS, where values would be stored in a queue and appended to the return list in the
order they were appended. However, I added a temporary list between each level of the tree and added
the node values in the corresponding level to the temporary list first before appending the temp
list to the return list.

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        rlist = []
        queue = []

        if root:
            queue.append(root)

        while queue:
            temp = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            rlist.append(temp)
            
        return rlist
        


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
