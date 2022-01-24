# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

	answer[i] % answer[j] == 0, or
	answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

Constraints:

	1 <= nums.length <= 1000
	1 <= nums[i] <= 2 * 109
	All the integers in nums are unique.
"""
from typing import List
import pytest
import pdb


"""
Try find recurrence
Exhaustive search
  - Timed out!

  - I'm probably searching too much, we must find out when we can skip a test.
  - search N^2 pairwise

"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        L = len(nums)
        if L <= 1:
            return nums
        nums.sort()
        # For table of divisible subset containing nums[i],
        dp = [[num] for num in nums]
        
        for i in range(len(nums)):
            # Check for nums[j] where adding nums[i] to dp[j] results in larger subset
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j])+1:
                    dp[i] = dp[j] + [nums[i]]

        # then return the largest set
        return max(dp, key=len)




@pytest.mark.parametrize('nums, target', [
    ([1,2,3],[1,2]),
    ([1,2,4,8], [1,2,4,8]),
    ([3,4,16,8], [4,8,16]),
    ([5,9,18,54,108,540,90,180,360,720], [9,18,90,180,360,720]),
    ([9,75,12,18,90,4,36,8,28,2], [2, 4, 12, 36])
])
def test(nums, target):
    assert sorted(Solution().largestDivisibleSubset(nums)) == sorted(target)

if __name__ == '__main__':
    #sys.exit(pytest.main(['-s', '-v'] + sys.argv))
    print(Solution().largestDivisibleSubset([9,75,12,18,90,4,36,8,28,2]))
