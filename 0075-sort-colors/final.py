"""
Approach:
I created buckets for each color. I ran through the nums list and added one counter for each color. 
I then created a pointer for the index of the list. For each color, I changed the corresponding nums
value for the pointer to the corresponding color, and incremented the pointer by one. I did this 
process the number of times shown by the corresponding value in the buckets list. 

Time Complexity:  O(n)
Space Complexity: O(1)

Tests:
[2,0,2,1,1,0] --> [0,0,1,1,2,2]
[2,0,1] --> [0,1,2]
"""

class Solution:
    def sortColors(self, nums):
        buckets = [0,0,0]
        for i in nums:
            buckets[i] += 1
        
        i=0

        for color in range(3):
            for number in range(buckets[color]):
                nums[i] = color
                i+=1


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
