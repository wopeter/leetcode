"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or grid ==[]:
            return 0
        queue = []
        res = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    queue.append((i, j))
                    while queue != []:
                        top = queue.pop(0)
                        grid[top[0]][top[1]] = "0"
                        queue.extend(self.surrounding(top, grid))
                    res += 1
        return res
                        
    def surrounding(self, index, grid):
        n, m = len(grid), len(grid[0])
        i, j = index[0], index[1]
        res = []
        if i+1 < n and grid[i+1][j] == "1":
            res.append((i+1, j))
        if i-1 > -1 and grid[i-1][j] == "1":
            res.append((i-1, j))
        if j+1 < m and grid[i][j+1] == "1":
            res.append((i, j+1))
        if j-1 > -1 and grid[i][j-1] == "1":
            res.append((i, j+1))
        return res
      
        