# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

Constraints:

	n == nums.length
	1 <= n <= 2 * 105
	-109 <= nums[i] <= 109
"""
import pytest
import math
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False

        key = -math.inf
        dec_stack = []
        for n in reversed(nums):
            if n < key:
                return True
            if not dec_stack or dec_stack[-1] >= n:
                dec_stack.append(n)
            else:
                while dec_stack and dec_stack[-1] < n:
                    key = dec_stack.pop()
                dec_stack.append(n)
        return False


@pytest.mark.parametrize("nums, expected", [([3, 1, 4, 2], True)])
def test(nums, expected):
    assert Solution().find132pattern(nums) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
