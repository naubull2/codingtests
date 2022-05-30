# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true
Example 2:
Input: n = 0
Output: false
Example 3:
Input: n = 9
Output: true
Example 4:
Input: n = 45
Output: false

Constraints:

	-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""
import pytest


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1. a simple loop until N
        if n == 1:
            return True
        num = 3
        while num < n:
            num *= 3
        if num == n:
            return True
        return False


# 2. Use the constraint. (No loop/recursion)
# maximum possible power of three is 3^20 < 2^31-1
# depends on system (sys.maxsize), but the problem gave us 2^31-1
"""
if n <= 0:
    return False

if 3**20 % n == 0:
    return True
return False
"""


@pytest.mark.parametrize("n, ispower", [(27, True), (0, False), (9, True), (45, False)])
def test(n, ispower):
    assert Solution().isPowerOfThree(n) == ispower


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
