"""
Approach:
I created a BFS with an added caveat: instead of popping elements from the front of the queue, it 
would pop elements from the end of the queue. Moreover, elements would only be appended to the 
return list if it was the first element in the level. 

Time Complexity:  O(n)
Space Complexity: O(n)

Issues:
Appends elements to the queue in the wrong order, leading to incorrect outputs in some cases.

Tests:
[1,2,3,null,5,null,4] --> [1,3,2,5], expected: [1,3,4]
[1,2,3,4,null,null,null,5] --> [1,3,4,5]
[1,null,3] --> [1,3]
[] --> []
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
            for i in range(len(queue)):
                curr = queue.pop()

                if i == 0:
                    rlist.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        return rlist


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
