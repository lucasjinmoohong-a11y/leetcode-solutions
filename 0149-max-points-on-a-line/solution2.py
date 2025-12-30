"""
Approach:
I created a copy of the "points" list to check at the end whether or not there is only one point in it.
Moreover, if there are no points  in the list, the function returns 0. 

Time Complexity:  O(n^3*20001)
Space Complexity: O(n)

Issues:
Some tests simply don't work in LeetCode. 

Tests:
[[3,10],[0,2]] --> 1, correct: 2
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
        original = points[:]
        maxes = []
        for point1 in points:
            points.pop(0)
            for point2 in points:
                maxes.append(self.line(point1, point2, points))
        if maxes:
            return max(maxes)
        elif original:
            return 1
        else:
            return 0


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
