# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
Example 3:
Input: nums = [1]
Output: 1

Constraints:

	1 <= nums.length <= 3 * 104
	-3 * 104 <= nums[i] <= 3 * 104
	Each element in the array appears twice except for one element which appears only once.
"""
import pytest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # think of same = 0 different = 1
        # then we have bit xor
        xor = 0
        for n in nums:
            xor ^= n
        return xor


@pytest.mark.parametrize("", [])
def test():
    pass


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
