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


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        [5, 7, 7, 8, 8, 10], target = 8
        [8, 8, 8, 8,... 8, 8, 8], target = 8
        10^5

        - modified binary search?
         - instead of looking for exact value,
           find value who's adjacent value is not 8 (left / right)
        
        2 binary searches

        """
        def binary_search(nums, target, is_left):
            #is_left : True  = target who's left adjacent value is not target
            #          False = target who's right adjacent value is not target
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if is_left:
                        if (
                            (mid-1 >= 0 and nums[mid-1] != target)
                            or mid == 0
                        ):
                            return mid
                        else:
                            r = mid - 1
                    else:
                        if (
                            (mid+1 < len(nums) and nums[mid+1] != target)
                            or (mid+1) == len(nums)
                        ):
                            return mid
                        else:
                            l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        return [binary_search(nums, target, True), binary_search(nums, target, False)]



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

if __name__ == "__main__":
    Solution().searchRange([2, 2], 2)
    #sys.exit(pytest.main(["-s", "-v"] + sys.argv))
