# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

	2 <= nums.length <= 105
	-30 <= nums[i] <= 30
	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
import pytest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
         Get all multiplied.. -> divide self from the total multiplication..
         -> but no division allowed!

         store partial multiplication result..
         create a 
         prefix multiplication
         suffix multiplication
         ->       ans[i] = prefix[:i] * suffix[i+1:]
         -> if we put prefix in the ouitput array, then grow a suffix multiplication by 
            scanning the array from behind O(1) ; ignoring the output array space

         arr [ 1  2  3  4 ]
         ans [ 1  2  6  24]
                        6  1
                     8  4
                  12 12
              24 24
         ans [24, 12, 8, 6]
        """
        temp = 1
        ans = []
        for n in nums:
            temp *= n
            ans.append(temp)

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i-1] * suffix if i > 0 else suffix
            suffix *= nums[i]
        return ans


@pytest.mark.parametrize('nums, output', [
    ([1,2,3,4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
])
def test(nums, output):
    assert Solution().productExceptSelf(nums) == output

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
