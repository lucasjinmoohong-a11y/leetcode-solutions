"""
Approach:
I next thought it was an issue with the fact that I was modifying the list while iterating over it. 
However, this still didn't work. I tried running the code in VS code, where it worked fine. 

Time Complexity:  O(n^3*20001)
Space Complexity: O(n)

Tests:
in LeetCode: [[3,10],[0,2]] --> 1, correct: 2
in VS Code: [[3,10],[0,2]] --> 2
--> problem with LeetCode running testcase
"""

class Solution(object):
    def line(self, p1, p2, points):
        counter=0
        if p1 == p2:
            return 1
        elif p1[0] == p2[0]:
            for y in range(-10000,10001):
                if [p1[0],y] in points:
                    counter+=1
        else:
            for x in range(-10000,10001):
                y = (p1[1] - p2[1]) / (p1[0] - p2[0]) * (x - p1[0]) + p1[1]
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
        maxes = []
        for point1 in points:
            for point2 in points:
                maxes.append(self.line(point1, point2, points))
        if maxes:
            return max(maxes)
        else:
            return 0


if __name__ == "__main__":
    sol = Solution()
    # Example test:
    # print(sol.<function_name>(...))
    print(sol.maxPoints([[3,10],[0,2]]))
