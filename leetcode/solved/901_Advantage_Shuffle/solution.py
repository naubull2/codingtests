# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two arrays nums1 and nums2 of equal size, the advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.

Example 1:

Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]

Example 2:

Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]

Note:

	1 <= nums1.length = nums2.length <= 10000
	0 <= nums1[i] <= 109
	0 <= nums2[i] <= 109
"""
import pytest
import pdb
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Assign the lowest possible n1 for n2.
        Leftovers are always  n2 > n1 anyway, so assign to whatever order.
        """
        pairs = {n2: [] for n2 in nums2}
        leftover = []
        i = 0
        sorted_nums2 = sorted(nums2)
        for n1 in sorted(nums1):
            if n1 > sorted_nums2[i]:
                pairs[sorted_nums2[i]].append(n1)
                i += 1
            else:
                leftover.append(n1)

        return [pairs[n2].pop() if pairs[n2] else leftover.pop() for n2 in nums2]


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        ([2, 7, 11, 15], [1, 10, 4, 11], [2, 11, 7, 15]),
        ([12, 24, 8, 32], [13, 25, 32, 11], [24, 32, 8, 12]),
        ([2, 0, 4, 1, 2], [1, 3, 0, 0, 2], [2, 0, 2, 1, 4]),
    ],
)
def test(num1, num2, expected):
    assert Solution().advantageCount(num1, num2) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
