"""
Approach:
Binary search: set a bottom and top pointer. While True, set a pointer in the middle of top
and bottom. If it is greater than the target (using the guess() function), then move the top pointer
down to mid - 1. If it is smaller, then move the bottom pointer up to mid + 1. If mid == target, then 
return mid.

Time Complexity:  O(log(n))
Space Complexity: O(1)
"""

def guess(x, your_guess):
    if your_guess > x:
        return -1
    elif your_guess < x:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n):
        bottom = 1
        top = n

        while True:
            mid = (bottom + top) // 2
            if guess(mid) > 0:
                bottom = mid + 1

            elif guess(mid) < 0:
                top = mid - 1

            else:
                return mid


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
