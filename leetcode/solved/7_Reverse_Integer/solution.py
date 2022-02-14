# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:

	-231 <= x <= 231 - 1
"""
import pytest


class Solution:
    def reverse(self, x: int) -> int:
        """Most leetcode solutions seem to ignore the fact that their codes may overflow in the system
        the problem has given: can't handle 32-bit+ integers (They simply return 0 when overflowed already)
           - It meets the online judge's condition, but not exactly the condition given in the problem statement.
        """
        sign = -1 if x < 0 else 1

        intmax = 2**31-1 if sign > 0 else 2**31
        
        val = x * sign
        out = 0
        while val:
            res = val % 10
            val //= 10
            # check overflow before it actually overflows!
            if out > (intmax - res) / 10:
                return 0
            out = out * 10 + res
        return out * sign
        
        
@pytest.mark.parametrize('x, output', [
    (123, 321),
    (-123, -321),
    (120, 21),
    (9009, 9009),
    (900, 9),
    (1534236469, 0),
    (1563847412, 0)
])
def test(x, output):
    assert Solution().reverse(x) == output

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
