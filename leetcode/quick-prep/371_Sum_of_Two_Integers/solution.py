# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3
Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:

	-1000 <= a, b <= 1000
"""
import pdb
import pytest


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFF # 12 bits of 1s = 4095
        SUM_MAX = 0x7FF # 11 bits of 1s = 2047
        
        # values in range [-1000, 1000] will be
        # less than 1024 => 11bit + 1sign bit => 12 bits mask == 0xFFF
        # inorder to mask carrys, at the maximum we need 1 more bit => 12bits
        while b != 0: # run until no carry
            sum_val = (a ^ b) & mask # like-bits equals 0
            carry = ((a & b)<<1) & mask   # 1,1 => 1 only
            a = sum_val
            b = carry 
        if a > SUM_MAX:
            a = ~(a ^ mask)
        return a


@pytest.mark.parametrize('a, b, result', [
    (-12, -8, -20)
])
def test(a, b, result):
    assert Solution().getSum(a, b) == result

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
