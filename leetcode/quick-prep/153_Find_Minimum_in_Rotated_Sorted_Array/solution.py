# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

	[4,5,6,7,0,1,2] if it was rotated 4 times.
	[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:

	n == nums.length
	1 <= n <= 5000
	-5000 <= nums[i] <= 5000
	All the integers of nums are unique.
	nums is sorted and rotated between 1 and n times.
"""
import pytest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [l, left, ...r][l,,.right...r]
                      ^
            if mid > r -> in the left half
               -> search right
            else
               <- search left

        When to stop?
         - when mid-1 > mid
         - when l < r : sorted portion
             - either the array is not rotated, or inside right half
             - WE will not be in left half as the target would be out of l~r range!

        TEST cases: [3, 4, 0, 1, 2]
                    [0, 1, 2]
             edge1  [4, 0, 1, 2, 3]
             edge2  [0]
        """
        l, r = 0, len(nums)-1
        while l <= r: # should include = as the array size may be 1
            mid = l + (r-l)//2

            # termination
            if nums[mid-1] >= nums[mid]: # may be [0]==[-1]
                return nums[mid]
            elif nums[l] < nums[r]:
                return nums[l]

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1


@pytest.mark.parametrize('nums, target', [
    ([3, 4, 0, 1, 2], 0),
    ([0, 1, 2], 0),
    ([4, 0, 1, 2, 3], 0),
    ([0], 0)
])
def test(nums, target):
    assert target == Solution().findMin(nums)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
