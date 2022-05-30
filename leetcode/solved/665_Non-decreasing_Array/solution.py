# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:

	n == nums.length
	1 <= n <= 104
	-105 <= nums[i] <= 105
"""
import pytest
import pdb
from typing import List


MIN = -(10**5)


class Solution:
    # Time : O(N), Space O(1)
    def checkPossibility(self, nums: List[int]) -> bool:
        fail_count = 0
        last = nums[0]
        for i in range(1, len(nums)):
            if last > nums[i]:
                fail_count += 1
                if (nums[i - 2] if i > 1 else MIN) <= nums[i]:
                    last = nums[i]
                elif (nums[i - 2] if i > 1 else MIN) <= last:
                    last = last
                else:
                    fail_count += 1

                if fail_count > 1:
                    return False
            else:
                last = nums[i]
        return True


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-58, -59, -67], False),
        ([4, 2, 1], False),
        ([4, 2, 3], True),
        ([3, 4, 2, 3], False),
        ([5, 7, 1, 8], True),
    ],
)
def test(nums, expected):
    assert Solution().checkPossibility(nums) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
