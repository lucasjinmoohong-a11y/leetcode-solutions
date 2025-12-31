"""
Approach:
I created a binary search algorithm that ran while the left pointer was less than or equal to the right
pointer. The algorithm created a middle pointer and checked whether or not it was a bad version. If it
was, it would set it as the first bad version (so far) and change the right pointer to mid - 1. If not,
it would set the left pointer to mid + 1. After left > right, it returned first. 

Time Complexity:  O(log(n))
Space Complexity: O(1)
"""

def isBadVersion(list, num):
    if num in list:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        first = 0

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                first = mid
                right = mid - 1

            else:
                left = mid + 1
        
        return first


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
