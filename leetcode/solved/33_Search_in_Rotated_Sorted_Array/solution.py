# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:

	1 <= nums.length <= 5000
	-104 <= nums[i] <= 104
	All values of nums are unique.
	nums is an ascending array that is possibly rotated.
	-104 <= target <= 104
"""
import pytest
import pdb
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        return self.bsearch(nums, left, right, target)
            
    
    def bsearch(self, nums, left, right, target):
        # handle terminal & edge cases 
        if left >= right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            return -1

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif mid == left and nums[right] == target:
            return right

        # Other standard cases
        pivot = 0 # no rotation
        if nums[left] > nums[right]:
            if nums[mid] < nums[right]:
                pivot = -1
            else:
                pivot = 1

        if nums[mid] > target:
            # edge
            if nums[left] > target and pivot == 1:
                return self.bsearch(nums, mid+1, right, target)
            # else
            return self.bsearch(nums, left, mid-1, target)
        else:
            # edge
            if nums[right] < target and pivot == -1:
                return self.bsearch(nums, left, mid-1, target)
            # else
            return self.bsearch(nums, mid+1, right, target)


@pytest.mark.parametrize('nums, target, expected', [
	([4,5,6,7,0,1,2], 0, 4),
	([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1),
    ([1,2,0], 1, 0),
    ([1,3], 3, 1),
    ([1,3,5], 5, 2),
    ([5, 1, 3], 5, 0),
    ([4,5,6,7,0,1,2],2, 6),
    ([4,5,6,7,8,1,2,3],8, 4)
])
def test(nums, target, expected):
	assert expected == Solution().search(nums, target)

if __name__ == '__main__':
    print(f'solution is : {Solution().search([4,5,6,7,8,1,2,3], 8)}')
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
