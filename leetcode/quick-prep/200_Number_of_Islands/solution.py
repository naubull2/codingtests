# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 300
	grid[i][j] is '0' or '1'.
"""
import pytest
from typing import List

        
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # keep a copy of grid, where we store visit flag
        M, N = len(grid), len(grid[0])
        visited = set()
        
        # then for some starting poitn that hasn't been visited,
        # we expand from thereon, using a BFS traversal where level is the distance away from the starting point
        def explore(i, j):
            tier = deque([(i,j)])
            visited.add((i,j))
            while tier:
                x, y = tier.popleft()
                
                for dx, dy in [(0,1), (0,-1), (1,0),(-1,0)]: # in 4 directions
                    if ((x+dx) not in range(M) 
                     or (y+dy) not in range(N)
                     or grid[x+dx][y+dy] == '0' 
                     or (x+dx, y+dy) in visited
                    ):
                        continue
                    else:
                        tier.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))

        islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1' and (i,j) not in visited:
                    islands += 1
                    explore(i,j)
        return islands


@pytest.mark.parametrize('grid, num', [
  ([["1","1","0","0","0"],["1","1","0","0","0"],
    ["0","0","1","0","0"],["0","0","0","1","1"]], 3)
])
def test(grid, num):
    assert Solution().numIslands(grid) == num

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
