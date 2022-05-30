# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

	The town judge trusts nobody.
	Everybody (except for the town judge) trusts the town judge.
	There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:

	1 <= n <= 1000
	0 <= trust.length <= 104
	trust[i].length == 2
	All the pairs of trust are unique.
	ai != bi
	1 <= ai, bi <= n
"""
import pytest
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = {i + 1: [] for i in range(n)}
        candidates = set({i + 1 for i in range(n)})
        for t in trust:
            trust_map[t[1]].append(t[0])
            if t[0] in candidates:
                candidates.remove(t[0])

        for c in candidates:
            if len(trust_map[c]) == n - 1:
                return c
        return -1


@pytest.mark.parametrize(
    "n, trust, expected",
    [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3),
    ],
)
def test(n, trust, expected):
    assert Solution().findJudge(n, trust) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
