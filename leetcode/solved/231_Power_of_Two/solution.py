# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

Constraints:

	-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""
import pytest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """Simply using the constraint
        if n > 0 and 2**31 % n == 0:
            return True
        return False
        """
        if n < 1:
            return False
        b = 1
        while b < n:
            b *= 2
        if b == n:
            return True
        return False


@pytest.mark.parametrize(
    "n, expected", [(1, True), (16, True), (3, False), (0, False), (-16, False)]
)
def test(n, expected):
    assert Solution().isPowerOfTwo(n) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
