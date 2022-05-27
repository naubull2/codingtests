# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

	1 <= n <= 45
"""
import pytest
from collections import deque

class Solution:
    def climbStairs(self, n: int) -> int:
        # tabular bottom up - instead of DP
        tb = [0, 1, 2]
        for i in range(3, n+1):
            tb.append(tb[i-1] + tb[i-2])
        return tb[n]

@pytest.mark.parametrize('n, output', [
	(38, 63245986),
	(3, 3),
	(20, 10946)
])
def test(n, output):
	assert output == Solution().climbStairs(n)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
