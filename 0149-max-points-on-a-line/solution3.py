"""
Approach:
I first thought it was a rounding error, because the slope is 8/3, which could get rounded to 2.66667. 
However, even after adding a rounding check, the function still outputted the wrong value. git

Time Complexity:  O(n^3*20001)
Space Complexity: O(n)

Issues:
Still returns 1 instead of 2. 

Tests:
[[3,10],[0,2]] --> 1, correct: 2
print statements:
when x == 0: y == 4, correct: 2
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
                if abs(y - round(y)) < 1e-9:
                    y = int(round(y))
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
