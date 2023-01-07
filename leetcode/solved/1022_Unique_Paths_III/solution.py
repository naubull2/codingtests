# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n integer array grid where grid[i][j] could be:

	1 representing the starting square. There is exactly one starting square.
	2 representing the ending square. There is exactly one ending square.
	0 representing empty squares we can walk over.
	-1 representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

grid [[1, 0, 0],
      [-1, -1, 0],
      [-1, -1, 2]]

Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 20
	1 <= m * n <= 20
	-1 <= grid[i][j] <= 2
	There is exactly one starting cell and one ending cell.
"""
import pytest
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        cells, p_init = 1, None # include 2 as path

        # Find starting point, count traversible cells
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    p_init = (i,j)
                elif grid[i][j] == 0:
                    cells += 1

        def get_next(i, j):
            #  traversible neighboring cells
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii, jj = i+dx, j+dy
                if (
                    0 <= ii and ii < M and
                    0 <= jj and jj < N and
                    grid[ii][jj] in {0, 2}
                ):
                    yield (ii, jj)

        def dfs(i, j, count):
            ans = 0
            if grid[i][j] == 2 and count == cells:
                ans += 1
                return ans
            if grid[i][j] in {0, 1}:
                grid[i][j] = -1
                for nei in get_next(i, j):
                    ans += dfs(*nei, count+1)
                grid[i][j] = 0
            return ans

        ans = dfs(*p_init, 0) 
        return ans


@pytest.mark.parametrize('grid, output', [
    ([[1, 0, 0], [-1, -1, 0], [-1, -1, 2]], 1)
])
def test(grid, output):
    assert output == Solution().uniquePathsIII(grid)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
