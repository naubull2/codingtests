# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

	1 <= nums.length <= 2 * 104
	-1000 <= nums[i] <= 1000
	-107 <= k <= 107
"""
import pytest
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        init: sum[i, j] would induce O(N^2) loops and O(N) summation => O(N^3)
        better than this?
        cummulative sum to reduce summation all the time => still O(N^2)

        Immprove from there?

        prefixsum[:j] - prefixsum[:i-1] = sum[i:j]

        sum[i:j] = k = prefixsum[:j] - prefixsum[:i-1]
        prefixsum[:j] -k = prefixsum[:i-1]

        - Create a hashmap of # of subarrays at i that sum to k.
        {i: 2} => we have two prefix sums that adds up to k for index up to i

        if j-k == i, then we add another 2 to the answer count

        from j -> {i:2} we have another sum to k (i1:j, i2:j)
        """
        cnt, run = 0, 0
        prefixsum = dict()
        prefixsum[0] = 1
        for n in nums:
            run += n
            cnt += prefixsum.get(run-k, 0)
            prefixsum[run] = prefixsum.setdefault(run, 0) + 1
        return cnt


@pytest.mark.parametrize('nums, k, target', [
    ([1, 1, 1], 2, 2),
    ([1,2,3], 3, 2)
])
def test(nums, k, target):
    assert target == Solution().subarraySum(nums, k)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
