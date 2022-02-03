# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

	For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.

Given an integer num, return its complement.

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

Constraints:

	1 <= num < 231

Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""
import pytest


class Solution:
    def findComplement(self, num: int) -> int:
        bits = []
        while num:
            bits.append((num & 1)^1)
            num = num >> 1
        if not bits:
            return 1
        return int(''.join([str(b) for b in bits][::-1]), 2) 
         


@pytest.mark.parametrize('num, output', [
    (5, 2),
    (1, 0),
    (2, 1)
])
def test(num, output):
    assert Solution().findComplement(num) == output

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
