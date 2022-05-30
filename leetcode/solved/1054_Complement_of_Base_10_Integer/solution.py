# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

	For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.

Given an integer n, return its complement.

Example 1:

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

Example 2:

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

Example 3:

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

Constraints:

	0 <= n < 109

Note: This question is the same as 476: https://leetcode.com/problems/number-complement/
"""
import pytest


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        output = 0
        for i, b in enumerate(bin(n)[2:][::-1]):
            output += (int(b) ^ 1) * 2**i
        return output


@pytest.mark.parametrize("n, output", [(5, 2), (7, 0), (10, 5)])
def test(n, output):
    assert Solution().bitwiseComplement(n) == output


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
