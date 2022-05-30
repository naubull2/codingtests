# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Constraints:

	1 <= time.length <= 6 * 104
	1 <= time[i] <= 500
"""
import pytest
from typing import List
from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """Works, but should timeout as this is a medium difficulty, and won't allow O(N^2)
        time_hash = Counter(time)

        targets = []
        n = 60
        while n <= 1000:
            targets.append(n)
            n += 60

        cnt = 0
        for t in time:
            for target in targets:
                counts = time_hash.get(target-t, 0)
                cnt += max(counts-1 if target-t == t else counts, 0)

        return cnt//2
        """
        # build a list of residuals
        cnts = [0] * 60
        for t in time:
            cnts[t % 60] += 1

        # cnts[0] and cnts[30] are self mirrored so num of combination is (n*(n+1)/2)
        def combination(n):
            return (n - 1) * n // 2

        pairs = 0
        for i in range(1, 30):  # so iterate on 1-29
            pairs += cnts[i] * cnts[60 - i]
        return pairs + combination(cnts[0]) + combination(cnts[30])


@pytest.mark.parametrize(
    "time, count",
    [
        ([30, 20, 150, 100, 40], 3),
        ([60, 60, 60], 3),
        ([15, 63, 451, 213, 37, 209, 343, 319], 1),
    ],
)
def test(time, count):
    assert Solution().numPairsDivisibleBy60(time) == count


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
