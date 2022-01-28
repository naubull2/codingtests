# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

	a, b are from arr
	a < b
	b - a equals to the minimum absolute difference of any two elements in arr

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

Constraints:

	2 <= arr.length <= 105
	-106 <= arr[i] <= 106
"""
import pytest
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mad = arr[-1]-arr[0]
        mad_arr = []
        for i, e in enumerate(arr[:-1]):
            diff = arr[i+1]-e
            if diff < mad:
                mad = diff
                mad_arr = [[e, arr[i+1]]]
            elif diff == mad:
                mad_arr.append([e, arr[i+1]])
        return mad_arr 


@pytest.mark.parametrize('arr, expected', [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]])
])
def test(arr, expected):
    assert Solution().minimumAbsDifference(arr) == expected

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
