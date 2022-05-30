# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
import pytest
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        bs, fs = [], []
        sq = [n**2 for n in nums]  # O(N)

        last = sq[0]
        for n in sq:
            if not bs:
                bs.append(n)
            elif last and last >= n:
                bs.append(n)
            else:
                while bs and bs[-1] < n:
                    fs.append(bs.pop())
                last = bs[-1] if bs else None
                fs.append(n)
            last = n
        if bs:
            fs.extend(bs[::-1])
        return fs


@pytest.mark.parametrize("nums, expected", [([-4, -4, -3], [9, 16, 16])])
def test(nums, expected):
    assert Solution().sortedSquares(nums) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
