# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32

Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

2, 1, 10

Constraints:

	1 <= x, y <= 100
	0 <= bound <= 106
"""
import pytest
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful = set()
        x_i = 1
        while x_i <= bound:
            y_j = 1
            while y_j <= bound:
                s = x_i + y_j
                if s <= bound:
                    powerful.add(s)
                y_j *= y
                if y_j == 1:
                    break
            x_i *= x
            if x_i == 1:
                break
        return list(powerful)


@pytest.mark.parametrize(
    "x, y, bound, expected",
    [
        (2, 3, 10, [2, 3, 4, 5, 7, 9, 10]),
        (3, 5, 15, [2, 4, 6, 8, 10, 14]),
        (2, 1, 10, [2, 3, 5, 9]),
    ],
)
def test(x, y, bound, expected):
    assert set(Solution().powerfulIntegers(x, y, bound)) == set(expected)


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
