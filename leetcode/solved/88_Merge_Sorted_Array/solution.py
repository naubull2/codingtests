# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:

	nums1.length == m + n
	nums2.length == n
	0 <= m, n <= 200
	1 <= m + n <= 200
	-109 <= nums1[i], nums2[j] <= 109

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
import pytest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1  # compare from behind since we have buffer in the back
        k = m + n - 1
        while j >= 0 and i >= 0:  # do until either array is exhausted
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        while j >= 0:  # only check when nums2 is remaining: nums1 is already sorted
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        return None


@pytest.mark.parametrize(
    "nums1, nums2, m, n, result",
    [([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3, [1, 2, 2, 3, 5, 6]), ([0], [1], 0, 1, [1])],
)
def test(nums1, nums2, m, n, result):
    Solution().merge(nums1, m, nums2, n)
    assert result == nums1


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
