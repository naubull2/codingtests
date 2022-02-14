# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	nums contains distinct values sorted in ascending order.
	-104 <= target <= 104
"""
import pytest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Basic binary search but only handle not-found differently
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return low


@pytest.mark.parametrize('nums, target, expected', [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, 2),
    ([2, 5], 5, 1),
    ([-1, 0, 5], 5, 2),
    ([-1, 0, 5], 2, 2)
])
def test(nums, target, expected):
    obj= Solution()
    assert obj.searchInsert(nums, target) == expected

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
