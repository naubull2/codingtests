# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:

    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
"""
import pytest
import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        An optimal quicksort would use a quickselect for pivot selection,
        instead, let's just avoid these 2 extrems.

        Edges
        - already sorted array (not practical)
        - array of only the same elements (can do)
        """
        # check edge case
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                break
            if i == len(nums)-1:
                return nums

        def quicksort(l, r, nums):
            if r <= l:
                return
            # pivot select
            rand_pivot = random.randint(l, r-1)
            nums[r-1], nums[rand_pivot] = nums[rand_pivot], nums[r-1]
            pivot = nums[r-1]
            j = l # next insertion index
            # iterative swaps
            for i in range(l, r-1):
                if nums[i] < pivot: # put i to j if less than pivot
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[r-1], nums[j] = nums[j], nums[r-1]

            # recurse into left/right splits
            quicksort(l, j, nums)
            quicksort(j+1, r, nums)

        quicksort(0, len(nums), nums)
        return nums


@pytest.mark.parametrize('arr, result', [
    ([2,2,2,2,2,2], [2,2,2,2,2,2]),
    ([3,1,4,6,4,5], [1,3,4,4,5,6])
])
def test(arr, result):
    assert Solution().sortArray(arr) == result

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
