# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:

Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16

Constraints:

	-104 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 104
"""
import pytest

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def get_overlap(range1, range2):
            if range1[0] < range2[0]:
                diff = range1[1] - range2[0]
                if range2[1] < range1[1]:
                    # complete subset
                    diff = range2[1] - range2[0]
            else:
                diff = range2[1] - range1[0]
                if range1[1] < range2[1]:
                    diff = range1[1] - range1[0]
                
            if diff > 0:
                return diff
            return 0
        
        x_overlap = get_overlap([ax1, ax2], [bx1, bx2])
        y_overlap = get_overlap([ay1, ay2], [by1, by2])
        intersection = x_overlap * y_overlap
        
        return (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) - intersection


@pytest.mark.parametrize('points, area', [
    ([0,0,0,0,-1,-1,1,1], 4)
])
def test(points, area):
    assert Solution().computeArea(*points) == area

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
