# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

	1 <= nums.length <= 105
	-231 <= nums[i] <= 231 - 1
	0 <= k <= 105

Follow up:

	Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
	Could you do it in-place with O(1) extra space?
"""
import pytest
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 1. simple pop -> insert operation
        while k:
            p = nums.pop()
            nums.insert(0, p)
            k -= 1
        
        
        # 2. buffer insert -> may fail when K is larger than the list size
        n = len(nums)
        shift = k % n
        if shift:
            nums[0:0] = nums[-shift:]
            while shift:
                nums.pop()
                shift -= 1
        
        # 3. combine 1 & 2 to improve 1's speed, cutting through redundant full rotations
        shift = k % len(nums)
        while shift:
            p = nums.pop()
            nums.insert(0, p)
            shift -= 1
        
        # 4. improve 2's approach by deallocating the trailing shift in batch
        shift = k % len(nums)
        if shift:
            nums[0:0] = nums[-shift:]
            del nums[-shift:]

        # 5. rather cheap, but using language specific feature, best optimized code
        k = k % len(nums)
        if not k:
            return
        nums[:] = nums[-k:] + nums[:-k]


        # 6. swap N into it's place
        N = len(nums)
        shift = k % N
        if not shift: return
        
        cnt, i = 0, 0
        while cnt < N:
            init, num = i, nums[i]
            while True: # k mod N loop
                next_pos = (i+shift) % N
                t = nums[next_pos]
                nums[next_pos] = num
                num = t
                i = next_pos
                cnt += 1
                if i == init: # loop again
                    i+=1
                    break

@pytest.mark.parametrize('nums, k, expected', [
    ([1], 0, [1]),
    ([99,-1,-100,3], 1, [3, 99, -1, -100]),
    ([-1], 2, [-1])
])
def test(nums, k, expected):
    Solution().rotate(nums, k)
    assert nums == expected

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
