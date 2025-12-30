"""
Approach:
I iterated through every combination of two points within the "points" list. For each combination, I 
run a function that creates a line between the two points and counts how many points are hit by the 
line. 

Time Complexity:  O(n^3*20001)
Space Complexity: O(n)

Issues:
When there is only one point in the "points" list, the function does not work because it is trying to 
find the max of an empty list.

Tests:
[[0,0]] --> ValueError: max() arg is an empty sequence
"""

class Solution(object):
    def line(self, p1, p2, points):
        counter=1
        if p1[0] == p2[0]:
            for y in range(-10000,10001):
                if [p1[0],y] in points:
                    counter+=1
        else:
            for x in range(-10000,10001):
                y = ((p1[1] - p2[1]) / (p1[0] - p2[0])) * (x - p1[0]) + p1[1]
                if [x,y] in points:
                    counter+=1
        return counter
    
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        maxes = []
        for point1 in points:
            points.pop(0)
            for point2 in points:
                maxes.append(self.line(point1, point2, points))
        return max(maxes)


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
