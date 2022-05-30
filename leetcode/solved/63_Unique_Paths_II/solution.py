# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:

	m == obstacleGrid.length
	n == obstacleGrid[i].length
	1 <= m, n <= 100
	obstacleGrid[i][j] is 0 or 1.
"""
from typing import List
import pytest


class Solution:
    # 1. Simple, readable way in O(2N) space
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        last_row = [0] * len(obstacleGrid[0])
        last_row[0] = 1
        curr_row = []
        for row in obstacleGrid:
            curr_row = []
            for i, col in enumerate(row):
                if col == 0:
                    curr_row.append(last_row[i] + (curr_row[i - 1] if i > 0 else 0))
                else:
                    curr_row.append(0)
            last_row = curr_row
        return curr_row[-1]

    # 2. In case of in-place storage
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #    # actually we might use the obstacleGrid itself
    #    if obstacleGrid[0][0] == 1:
    #        return 0
    #    else:
    #        obstacleGrid[0][0] = 1
    #    m = len(obstacleGrid)
    #    n = len(obstacleGrid[0])
    #    for j in range(1, n):
    #        obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

    #    for row in range(1, m):
    #        for j in range(n):
    #            if obstacleGrid[row][j] == 0:
    #                obstacleGrid[row][j] = (obstacleGrid[row-1][j] + obstacleGrid[row][j-1]
    #                                         if j > 0 else
    #                                        obstacleGrid[row-1][j])
    #            else:
    #                obstacleGrid[row][j] = 0
    #    return obstacleGrid[m-1][n-1]


@pytest.mark.parametrize(
    "grid, num_paths",
    [
        ([[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]], 10),
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
        ([[0, 0], [1, 0]], 1),
        ([[0, 0]], 1),
    ],
)
def test(grid, num_paths):
    assert Solution().uniquePathsWithObstacles(grid) == num_paths


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
