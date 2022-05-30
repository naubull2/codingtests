# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:

Input: matrix = [["0"]]
Output: 0

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 300
	matrix[i][j] is '0' or '1'.
"""
import pytest
from typing import List
import numpy as np


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # First setup border
        M, N = len(matrix), len(matrix[0])
        ms = [[int(col) for col in row] for row in matrix]
        maximal = int(any(any(row) for row in ms))
        # iterate from inside to out
        if N > 1 and M > 1:
            for i in range(len(matrix) - 2, -1, -1):
                for j in range(len(matrix[0]) - 2, -1, -1):
                    if ms[i][j] == 1:
                        if ms[i + 1][j] == ms[i][j + 1]:
                            edge = ms[i + 1][j]
                            if ms[i + edge][j + edge] > 0:
                                ms[i][j] = ms[i + 1][j] + 1
                            else:
                                ms[i][j] = ms[i][j + 1]
                        else:
                            ms[i][j] = 1 + min(ms[i][j + 1], ms[i + 1][j])
                    else:
                        ms[i][j] = 0
                    maximal = max(maximal, ms[i][j])
        return maximal**2


@pytest.mark.parametrize(
    "matrix, expected",
    [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
        ),
        ([["0", "1"], ["1", "0"]], 1),
        (
            [
                ["1", "1", "1", "1", "1", "1", "1", "1"],
                ["1", "1", "1", "1", "1", "1", "1", "0"],
                ["1", "1", "1", "1", "1", "1", "1", "0"],
                ["1", "1", "1", "1", "1", "0", "0", "0"],
                ["0", "1", "1", "1", "1", "0", "0", "0"],
            ],
            16,
        ),
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "1", "1", "0"],
                ["1", "1", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["0", "0", "1", "1", "1"],
            ],
            16,
        ),
        (
            [
                ["0", "0", "1", "0"],
                ["1", "1", "1", "1"],
                ["1", "1", "1", "1"],
                ["1", "1", "1", "0"],
                ["1", "1", "0", "0"],
                ["1", "1", "1", "1"],
                ["1", "1", "1", "0"],
            ],
            9,
        ),
    ],
)
def test(matrix, expected):
    assert Solution().maximalSquare(matrix) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
