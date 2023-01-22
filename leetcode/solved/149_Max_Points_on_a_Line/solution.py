# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:

	1 <= points.length <= 300
	points[i].length == 2
	-104 <= xi, yi <= 104
	All the points are unique.
"""
import pytest
from collections import defaultdict
from typing import List
from math import inf


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def gradient(pa, pb):
            if pa[0] == pb[0]:
                return inf
            return (pb[1]-pa[1])/(pb[0]-pa[0])

        ans = 0
        for i in range(len(points)-1):
            count = defaultdict(lambda:1) # point i is always included 
            for j in range(i+1, len(points)):
                count[gradient(points[i], points[j])] += 1
            if count:
                ans = max(max(count.values()), ans)
        return ans


@pytest.mark.parametrize('points, count', [
    ([[0,0], [0, 1]], 2),
    ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4)
])
def test(points, count):
    assert Solution().maxPoints(points) == count


if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
