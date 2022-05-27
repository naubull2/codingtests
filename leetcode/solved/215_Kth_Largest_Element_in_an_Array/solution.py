# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

	1 <= k <= nums.length <= 104
	-104 <= nums[i] <= 104
"""
import pytest
from typing import List
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. Simplest/naive approach is to sort
        # O(nlogn)
        # nums.sort()
        # return nums[-k]

        # 2. But we don't need all elements in order, only k largest.
        # Use min-heap to keep K largest, removing smallest in the heap onthe fly
        q = []
        for n in nums:
            heappush(q, n) # logK
            if len(q) > k:
                heappop(q) # logk
        return q[0]


@pytest.mark.parametrize('arr, k, val', [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4)
])
def test(arr, k, val):
    assert Solution().findKthLargest(arr, k) == val

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
