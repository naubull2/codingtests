# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:

	1 <= s.length <= 16
	s contains only lowercase English letters.
"""
import pytest
from typing import List
from functools import lru_cache


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        # custom cache works much faster than lru_cache (functools)
        cache = {}

        def subset(s):
            if s in cache:
                return cache[s]
            if not s:
                return []
            elif len(s) == 1:
                cache[s] = [[s[0]]]
                return cache[s]
            else:
                candidates = []
                if palindrome(s):
                    candidates.append([s])

                for i in range(1, len(s)):
                    if palindrome(s[:i]):
                        candidates.extend([[s[:i]] + l for l in subset(s[i:])])
                cache[s] = candidates
                return candidates

        return subset(s)


@pytest.mark.parametrize(
    "s, output",
    [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        (
            "aabaa",
            [
                ["a", "a", "b", "a", "a"],
                ["a", "a", "b", "aa"],
                ["aa", "b", "a", "a"],
                ["aa", "b", "aa"],
                ["a", "aba", "a"],
                ["aabaa"],
            ],
        ),
        (
            "ffff",
            [
                ["ffff"],
                ["f", "fff"],
                ["f", "f", "ff"],
                ["f", "f", "f", "f"],
                ["f", "ff", "f"],
                ["ff", "ff"],
                ["ff", "f", "f"],
                ["fff", "f"],
            ],
        ),
    ],
)
def test(s, output):
    assert sorted(Solution().partition(s)) == sorted(output)


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
