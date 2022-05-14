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
        N = len(nums)
        if N < 3:
            return []
        nums.sort()
        ans = []
        
        # Instaed of using a hash table, we want to find a condition when duplicates occur
        
        # O(N^2)
        last = None
        pdb.set_trace()
        for i in range(N-2):
            
            target = -nums[i]
            if target == last:
                continue
            last = target
            j, k = i+1, N-1
            # now we search space while
            last2 = None
            while j < k:
                sum_jk = nums[j] + nums[k]
                if (nums[j], nums[k]) == last2:
                    j += 1
                    k -= 1
                    continue
                elif sum_jk == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    last2 = (nums[j], nums[k])
                    j += 1
                    k -= 1
                elif sum_jk < target:
                    j += 1
                else:
                    k -= 1
        return ans        
            

@pytest.mark.parametrize('nums, ans', [
    ([0,0,0,0], [[0,0,0]])
])
def test(nums, ans):
    assert ans == Solution().threeSum(nums)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
