# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:

	1 <= nums.length <= 104
	-109 <= nums[i] <= 109
"""
import pytest
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        for _ in range(2):
            for i in range(len(nums)):
                # 2 loops to ensure circular lookup
                while stack and nums[stack[-1]] < nums[i]:
                    # find the closest(lookback) that satisfy the condition
                    ans[stack.pop()] = nums[i]

                stack.append(i)
        return ans



@pytest.mark.parametrize('nums, expected', [
    ([1,2,1], [2, -1, 2]),
    ([1,2,3,4,3], [2, 3, 4,-1,4])
])
def test(nums, expected):
    assert Solution().nextGreaterElements(nums) == expected
