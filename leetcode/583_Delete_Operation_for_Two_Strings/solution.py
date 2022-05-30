# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:

	1 <= word1.length, word2.length <= 500
	word1 and word2 consist of only lowercase English letters.
"""
import pytest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass


@pytest.mark.parametrize("", [])
def test():
    pass


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
