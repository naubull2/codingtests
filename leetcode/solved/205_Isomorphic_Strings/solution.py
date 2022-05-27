# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:

	1 <= s.length <= 5 * 104
	t.length == s.length
	s and t consist of any valid ascii character.
"""
import pytest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        forward = dict()
        reverse = dict()
        for c1, c2 in zip(s, t):
            if c1 in forward or c2 in reverse:
                if c1 in forward and c2 in reverse:
                    if forward[c1] == c2 and reverse[c2] == c1:
                        continue
                return False
            else:
                forward[c1] = c2
                reverse[c2] = c1
        return True


@pytest.mark.parametrize('s, t, isTrue', [
    ('egg', 'add', True),
    ('badc', 'baba', False),
    ('paper', 'title', True),
    ('cutter', 'putter', True),
    ('map', 'cart', False)
])
def test(s, t, isTrue):
    assert isTrue == Solution().isIsomorphic(s, t)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
