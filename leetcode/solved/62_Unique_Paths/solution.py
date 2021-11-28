# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28

Example 4:

Input: m = 3, n = 3
Output: 6

Constraints:

	1 <= m, n <= 100
	It's guaranteed that the answer will be less than or equal to 2 * 109.
"""
import pytest
from math import factorial as fact


# As a mathematical solution.
#class Solution:
#    def uniquePaths(self, m: int, n: int) -> int:
#        M, N = m-1, n-1
#        return fact(M+N)//(fact(M) * fact(N))


# As a dynamic programming solution.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n]*m
        for i in range(0, m):
            for j in range(0, n):
                if not i or not j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1] 



@pytest.mark.parametrize('m, n, output', [
    (3, 7, 28),
    (3, 2, 3)
])
def test(m, n, output):
    pass

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
