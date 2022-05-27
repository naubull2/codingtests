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
        sign = 1 if x > 0 else -1
        div = x if x > 0 else -x
        digits = []
        while div:
            div, mod = divmod(div, 10)
            digits.append(mod)
    
        INTMAX = pow(2, 31)-1 if sign > 0 else pow(2, 31)
        
        ans = 0
        scale = 1
        while digits:
            d = digits.pop()
            if d > (INTMAX - ans)/scale:
                # overflow
                return 0
            ans = scale * d + ans
            scale *= 10
        return sign * ans


@pytest.mark.parametrize('integer, result', [
    (123, 321),
    (-123, -321),
    (120, 21)
])
def test(integer, result):
    assert Solution().reverse(integer) == result

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
