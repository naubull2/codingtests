# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

	0 <= nums.length <= 105
	-109 <= nums[i] <= 109
	nums is a non-decreasing array.
	-109 <= target <= 109
"""
import pytest
import pdb
from typing import List


# NOTE: ordinary binary search for comparison
def bsearch(nums, target, left, right):
    mid = (left + right) // 2
    if left < right and left < mid:
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return bsearch(nums, target, mid, right)
        else:
            return bsearch(nums, target, left, mid)
    else:
        try:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
        except:
            return -1
        return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # search middle
        mid = self.find_bsearch(nums, target, 0, len(nums) - 1, None)
        if mid < 0:
            return [-1, -1]
        right = self.find_bsearch(nums, target, mid, len(nums) - 1, direction=1)
        left = self.find_bsearch(nums, target, 0, mid, direction=-1)
        return [min(left, mid), max(mid, right)]

    def find_bsearch(self, nums, target, left, right, direction=None):
        """Directed binary search when direction is given as [1 or -1]
        Set direction=None, for an ordinary binary search
        """
        mid = (left + right) // 2
        if left < right and left < mid:
            if nums[mid] == target:
                if not direction and nums[mid] == target:
                    return mid
                elif direction == 1:
                    return self.find_bsearch(nums, target, mid, right, direction)
                else:
                    return self.find_bsearch(nums, target, left, mid, direction)

            if nums[mid] < target:
                return self.find_bsearch(nums, target, mid, right, direction)
            else:
                return self.find_bsearch(nums, target, left, mid, direction)
        else:
            if not direction:
                try:
                    if nums[left] == target:
                        return left
                    elif nums[right] == target:
                        return right
                except:
                    return -1
                return -1
            if direction == 1 and nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            else:
                return right


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([2, 2], 2, [0, 1]),
        ([1, 1, 2], 1, [0, 1]),
        ([1, 2, 3, 3, 3, 3, 4, 5, 9], 3, [2, 5]),
        ([0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8], 4, [10, 12]),
    ],
)
def test(nums, target, expected):
    assert Solution().searchRange(nums, target) == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, 3),
        ([5, 7, 7, 8, 8, 10], 6, -1),
        ([], 0, -1),
        ([1, 4], 4, 1),
    ],
)
def test_binary_search(nums, target, expected):
    assert bsearch(nums, target, 0, len(nums) - 1) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
