# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

	1 <= nums.length <= 104
	-104 < nums[i], target < 104
	All the integers in nums are unique.
	nums is sorted in ascending order.
"""
from typing import List
import sys
import pytest
import pdb


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = len(nums)//2
        while True:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
                mid = (left+right)//2
            else:
                left = mid
                mid = (left+right)//2

            if mid == left or mid == right or left >= right:
                break
        if nums[mid] == target:
            return mid
        if left+1 == right and nums[right] == target:
            return right
        return -1


@pytest.mark.parametrize('nums, target, expected', [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1),
    ([2, 5], 2, 0),
    ([-1, 0, 5], 5, 2),
    ([-1, 0, 5], 2, -1)
])
def test(nums, target, expected):
    obj= Solution()
    assert obj.search(nums, target) == expected

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
