# coding: utf-8
# Copyright © 2023 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

	1 <= s.length <= 1000
	s consist of only digits and English letters.
"""
import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = (0, 0)
        for i in range(len(s)):
            for l, r in [(i, i), (i, i+1)]:
                while (
                    0 <= l and r < len(s) and
                    s[l] == s[r]
                ):
                    if (r - l) > (ans[1] - ans[0]):
                        ans = (l, r)
                    l -= 1
                    r += 1
        return s[ans[0]:ans[1]+1]


@pytest.mark.parametrize('s, sub', [
    ("babad", "bab"),
    ("cbbd", "bb")
])
def test(s, sub):
    assert Solution().longestPalindrome(s) == sub
