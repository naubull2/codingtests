# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0

Constraints:

	3 <= nums.length <= 1000
	-1000 <= nums[i] <= 1000
	-104 <= target <= 104
"""
import pytest
from typing import List
from math import inf


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = inf
        for i, n in enumerate(nums):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                tsum = n + nums[lo] + nums[hi]
                cur_diff = target - tsum
                if abs(cur_diff) < abs(diff):
                    diff = cur_diff
                if tsum < target:
                    lo += 1
                else:
                    hi -= 1
                if diff == 0:
                    break
        return target - diff


@pytest.mark.parametrize("nums, target, expect", [([-1, 2, 1, -4], 1, 2)])
def test(nums, target, expect):
    assert Solution().threeSumClosest(nums, target) == expect


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
