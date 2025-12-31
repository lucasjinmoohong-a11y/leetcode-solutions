"""
Approach:
I first created pointers for the top/bottom row and the left/right element of each row. From there, 
while top < bottom (ie top != bottom), I would calculate the middle row and compare its first element
to the target value. If it was greater than the target, the bottom pointer would be pushed up to mrow
(not mrow - 1 because that could go out of bounds). If it was less than the target, the top pointer
would be pushed to mrow + 1. Finally, if they were equal, then we would have found the right value. 

From there, after we found the right row, the code would run a binary search algorithm within the row. 

Time Complexity:  O(log(m*n))
Space Complexity: O(1)

Issues:
It gave wrong values. 

Tests:
[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3 --> False, correct answer: True
[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13 --> False
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while top < bottom: 
            mrow = (top + bottom) // 2 
            if matrix[mrow][0] > target:
                bottom = mrow # NOT mrow - 1 BC CAN GO OUT OF BOUNDS

            elif matrix[mrow][0] < target:
                top = mrow + 1 

            else:
                return True
        
        while left <= right:
            middle = (left + right) // 2
            if matrix[top][middle] > target:
                right = middle - 1
            
            elif matrix[top][middle] < target:
                left = middle + 1
            
            else:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
