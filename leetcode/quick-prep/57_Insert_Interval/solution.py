# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

	0 <= intervals.length <= 104
	intervals[i].length == 2
	0 <= starti <= endi <= 105
	intervals is sorted by starti in ascending order.
	newInterval.length == 2
	0 <= start <= end <= 105
"""
import pytest
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # clarification: 
        # no intervals overlap, even after inserting new interval this must hold true.
        ans = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # newOne < interval[i]  => insert the newOne and exit loop
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans
            elif newInterval[0] > intervals[i][1]:  # interval[i] < newOne => insert the interval[i] then continue
                ans.append(intervals[i])
            else:  # overlapping => update merged newONe and continue
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        ans.append(newInterval)
        return ans

@pytest.mark.parametrize('arr, new_one, result', [
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]])
])
def test(arr, new_one, result):
    assert result == Solution().insert(arr, new_one)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
