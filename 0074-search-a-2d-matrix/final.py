"""
Approach:
I changed the comparison when finding the right row; rather than checking the first element of mrow, 
I changed it to checking the first element if seeing whether it was larger than the target and 
checking the last element if seeing if it was smaller than the target. Moreover, if none were True, 
then the value must be in the row, so I set both top/bottom to mrow. 

Time Complexity:  O(log(m*n))
Space Complexity: O(1)

Tests:
[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3 --> True
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
                bottom = mrow

            elif matrix[mrow][right] < target: # changed comparison from 0 to right
                top = mrow + 1

            else:
                top = mrow # changed from return True to setting top/bottom to mrow
                bottom = mrow
        
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
