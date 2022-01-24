# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:

	1 <= s.length <= 500
	s consists of only lowercase English letters.
"""
import pytest


class Solution:
    def maxPower(self, s: str) -> int:
        maximal = 1
        curr, prev_c = 1, ''
        for i, c in enumerate(s):
            if prev_c == c:
                curr += 1
                maximal = max(maximal, curr)
            else:
                prev_c = c
                curr = 1
        return maximal


@pytest.mark.parametrize('string, power', [
    ('leetcode', 2),
    ('abbcccddddeeeeedcba', 5)
])
def test(string, power):
    assert Solution().maxPower(string) == power


if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
