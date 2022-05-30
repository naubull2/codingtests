# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:

	1 <= s.length <= 1000
	s consists of lowercase English letters.
"""
import pytest


class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i, j, s):
            cnt = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                cnt += 1
            return cnt

        return sum([expand(i, i, s) + expand(i, i + 1, s) for i in range(len(s))])


@pytest.mark.parametrize("string, count", [("aaa", 6), ("abc", 3)])
def test(string, count):
    assert Solution().countSubstrings(string) == count


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
