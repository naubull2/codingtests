# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] <= 105
"""
from typing import List
import pytest
import sys
import pdb


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search
        N = len(nums)
        if N == 1:
            return nums[0]
        i, j = 0, N-1
        while i < j:
            mid = (i + j) // 2
            odd = bool(mid % 2)
            if nums[mid] != nums[max(0, mid-1)] and nums[mid] != nums[min(mid+1, N-1)]:
                return nums[mid]
            elif nums[mid] == nums[max(0, mid-1)]:
                if odd:
                    i = mid
                else:
                    j = mid
            else:
                if odd:
                    j = mid
                else:
                    i = mid
            if i == mid and j == i+1:
                return nums[j]
            elif j == mid and i == j-1:
                return nums[i]
        return nums[mid]

            


@pytest.mark.parametrize('nums, output', [
    ([1,1,2,3,3,4,4,8,8], 2),
    ([3,3,7,7,10,11,11], 10),
    ([1], 1),
    ([1,1,2], 2),
    ([1,1,2,2,3], 3)
])
def test(nums, output):
    assert Solution().singleNonDuplicate(nums) == output

if __name__ == '__main__':
    #sys.exit(pytest.main(['-s', '-v'] + sys.argv))
    print(Solution().singleNonDuplicate([1,1,2]))
