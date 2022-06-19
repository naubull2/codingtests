# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] <= 109
	0 <= sum(nums[i]) <= 231 - 1
	1 <= k <= 231 - 1
"""
import pytest
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # keep a hashmap / hashset of prev_prefix_sum's remainder
        # when we hit current prefix_sum whos remainder is the same as anything in the hash, we have k's multiple
        prev_prefix_sum = nums[0]
        prefix_sum = 0
        hash_set = {0} # divisible by k
        for i in range(1, len(nums)):
            prefix_sum = prev_prefix_sum + nums[i]
            if prefix_sum %k in hash_set:
                return True
            hash_set.add(prev_prefix_sum % k)
            prev_prefix_sum = prefix_sum
        return False


@pytest.mark.parametrize('nums, k, result', [
    ([23,2, 6, 4, 7], 6, True),
    ([23,2, 6, 4, 7], 13, False),
    ([23,2, 4, 6, 7], 6, True)

])
def test(nums, k, result):
    assert result == Solution().checkSubarraySum(nums, k)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
