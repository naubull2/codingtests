# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []

Constraints:

	0 <= nums.length <= 3000
	-105 <= nums[i] <= 105
"""
import pytest
import pdb
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The basic logic would go about as the following
        # handle empty/non-valid cases
        N = len(nums)
        if N < 3:
            return []

        # O(NlogN) : sorting to utilize i<j<k, nums[i]<nums[j]<nums[k] property
        nums.sort()
        ans = []

        # for each nums[i]
        #
        # condition 1
        # no duplicates allowed; for any <nums[i], nums[j], nums[k]>
        # we can't have
        # ex. [1,1,1,2,2,3,4,4,5]
        #      i     j     k
        #        i   j     k
        #          i   j     k
        # if [1, 2, 4] is an answer,
        # are all duplicates

        # for the same nums[i] we skip (continue the loop)
        # for the same pair (nums[j], nums[k]) we skip the loop as well
        # j+1, k-1

        # Run hand tests
        # [-1, 0, -1, 2, 3, 4]
        # sorted: [-1, -1, 0, 2, 3, 4]
        #           i   j           k
        #
        last = None
        for i in range(N - 2):
            # set j, k to be i+1, N-1  setting i as the left most element
            target = -nums[i]
            if last == target:  # same nums[i] is a duplicate
                continue
            last = target

            j, k = i + 1, N - 1
            # 2-pointer approach (the same exact solution as in 2sum problem
            last_pair = None
            while j < k:
                sum_jk = nums[j] + nums[k]
                if target == sum_jk:
                    ans.append([nums[i], nums[j], nums[k]])
                    last_pair = (nums[j], nums[k])
                    j += 1
                    k -= 1
                elif (nums[j], nums[k]) == last_pair:
                    j += 1
                    k -= 1
                elif sum_jk < target:
                    j += 1
                else:
                    k -= 1
        return ans


@pytest.mark.parametrize(
    "nums, ans",
    [([0, 0, 0, 0], [[0, 0, 0]]), ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]])],
)
def test(nums, ans):
    sol = Solution().threeSum(nums)
    sol.sort(key=lambda x: sorted(x))
    ans.sort(key=lambda x: sorted(x))
    for s, a in zip(sol, ans):
        assert s == a


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
