"""
No 54.Spiral Matrix


Description
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == []:
            return res
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while up <= down and left <= right:
            if up == down:
                res.extend(matrix[up][left:right+1])
                return res
            if left == right:
                for i in range(up, down+1):
                    res.append(matrixp[i][left])
                return res
            for i in range(left, right):
                res.append(matrix[up][i])
            for j in range(up, down):
                res.append(matrix[j][right])
            for k in range(right, left, -1):
                res.append(matrix[down][k])
            for l in range(down, up, -1):
                res.append(matrix[l][left])
            up, down, left, right = up+1, down-1, left+1, right-1
        return res
        
        
        