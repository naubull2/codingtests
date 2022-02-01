# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:

	1 <= nums.length <= 200
	1 <= nums[i] <= 100
"""
import pytest
from typing import List
from collections import Counter


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: # no odd sum can be partitioned in to two subsets
            return False

        target = total/2

        nums.sort(reverse=True)

        ## DFS into search tree
        def find_sum(combo, rest, target):
            net = sum(combo)
            if net == target:
                return True
            elif net < target:
                return any(find_sum(combo + [n], [e for j, e in enumerate(rest) if j != i], target)
                           for i, n in enumerate(rest))
            else:
                # On largest value exceeding the half
                return False
        return find_sum([], nums, target)
                


@pytest.mark.parametrize('nums, result', [
    ([1,1,1,1], True),
    ([2,2,3,3,3,4,5], True), # [2, 4, 5], [2, 3, 3, 3]
    ([1,5,11,5], True),
    ([1,2,3,5], False),
    ([3,3,3,4,5], True)
])
def test(nums, result):
    assert Solution().canPartition(nums) == result

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
