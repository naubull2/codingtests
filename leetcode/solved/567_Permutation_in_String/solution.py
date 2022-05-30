# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

	1 <= s1.length, s2.length <= 104
	s1 and s2 consist of lowercase English letters.
"""
import pytest

from collections import Counter, deque


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        offset = {key: deque() for key in count.keys()}
        i = 0  # starting offset
        for j, c in enumerate(list(s2)):
            if c not in count:
                for char in s2[i : j + 1]:
                    if char in count:
                        count[char] += 1
                        offset[char].popleft()
                i = j + 1
            else:
                offset[c].append(j)
                if not count[c]:
                    last = offset[c].popleft()
                    for char in s2[i : last + 1]:
                        if char in count:
                            count[char] += 1
                            if char != c and offset[char]:
                                offset[char].popleft()
                    i = last + 1
                count[c] -= 1
            if all(v == 0 for v in count.values()):
                return True
        return False


@pytest.mark.parametrize(
    "s1, s2, output",
    [
        ("abc", "bbbca", True),
        ("ab", "eidbooaooo", False),
        ("ab", "eidbaoaooo", True),
        ("rmqqh", "nrsqrqhrymf", False),
        ("hello", "ooolleoooleh", False),
    ],
)
def test(s1, s2, output):
    assert output == Solution().checkInclusion(s1, s2)


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
