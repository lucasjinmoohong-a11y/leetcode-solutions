"""
Approach:
I implemented a more traditional BFS, with a temporary list made each layer. From there, the only 
element that would be appended to the return list would be the final element of the temp list. 

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
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
            rlist.append(temp[-1])
            
        return rlist


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))

