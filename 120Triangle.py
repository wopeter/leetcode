"""
Description

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

class solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        temp = []
        n = len(triangle)
        for i in range(n-1, -1, -1):
            r = triangle[i]
            if i == n-1:
                temp = r[:]
                continue
            for j in range(i+1):
                temp[j] = min(temp[j]+r[j], temp[j+1]+r[j])
                
        return temp[0]