# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:

Input: x = 3, y = 1
Output: 1

Constraints:

	0 <= x, y <= 231 - 1
"""
import pytest


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Either composing a list of binary bits or simple bit operation both would work
        z = x ^ y
        count = 0
        while z > 0:
            count += z % 2
            z //= 2
        return count


@pytest.mark.parametrize("x, y, expected", [(3, 1, 1)])
def test(x, y, expected):
    assert Solution().hammingDistance(x, y) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
