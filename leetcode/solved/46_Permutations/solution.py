# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:

	1 <= nums.length <= 6
	-10 <= nums[i] <= 10
	All the integers of nums are unique.
"""
import pytest
from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Tree search with BFS
        N = len(nums)
        level = deque([([], nums)])
        ans = []
        while level:
            candidate, rest = level.popleft()
            for i, e in enumerate(rest):
                expansion = candidate + [e]
                if len(expansion) == N:
                    ans.append(expansion)
                else:
                    level.append((expansion, rest[:j] + rest[j + 1 :]))
        return ans


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
