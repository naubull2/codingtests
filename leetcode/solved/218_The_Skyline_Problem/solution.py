# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

	lefti is the x coordinate of the left edge of the ith building.
	righti is the x coordinate of the right edge of the ith building.
	heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

Constraints:

	1 <= buildings.length <= 104
	0 <= lefti < righti <= 231 - 1
	1 <= heighti <= 231 - 1
	buildings is sorted by lefti in non-decreasing order.
"""
import pytest
import pdb
from typing import List
import heapq
# NOTE: min-heap we invert values to negatives to achieve max-heap
# we can implement the above data structure as array, where left, right childs are accessed by 2k+1, 2k+2 (0 indexed arrays)

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """Easy to understand but O(N**2)
        heap = [0] # initially max height is 0
        
        coords = []
        
        for l, r, h in buildings:
            coords.append((l, -h)) # -h represents start of building
            coords.append((r, h)) # +h represents end of building
        
        coords.sort() # sort by x coord followed by y coord (height)
        result = []

        for coord, h in coords:
            prev_max = heap[0] # keep track of prev max to see whether there is any change due to new building's ending or starting
            if h > 0: # if a building ends at this point 
                heap.remove(-h) # we should remove it from heap  O(N)
                heapify(heap)  # O(klogk)
            else:
                heappush(heap, h) # O(logk)

            if prev_max != heap[0]: # if max has changed in heap
                result.append((coord, -heap[0])) # we should add this to result

        return result
        """
        
        """Quite fuzzy, but runs crazy fast
        """
        N, hs = len(buildings), []
        for i, (l, r, h) in enumerate(buildings):
            # track i as building number
            hs.append((l, 0, -h, i))
            hs.append((r, 1, h, i))
        hs.sort() 
        alive = [False] * N # check if building is still there
        
        res, heap, current_height = [], [], 0
        for x, tp, h, i in hs: 
            if tp == 0:  # start of i-th building
                heapq.heappush(heap, (h, i))
                alive[i] = True
                if current_height < -h:
                    res.append([x, -h])
                    current_height = -h
            else:  # end of i-th building
                alive[i] = False
                # remove any buildings that is already done : including current building
                while heap and not alive[heap[0][1]]:
                    heapq.heappop(heap)  
                if heap and -heap[0][0] < current_height:
                    current_height = -heap[0][0]
                    res.append([x, current_height])
                elif not heap:
                    current_height = 0 
                    res.append([x, current_height])
        return res
        

@pytest.mark.parametrize('input, output', [
    ([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]], [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
    ([[0,2,3],[2,5,3]], [[0,3], [5, 0]])
])
def test(input, output):
    assert(Solution().getSkyline(input) == output)

if __name__ == '__main__':
    print(Solution().getSkyline([[0,3,3],[1,5,3],[2,4,3],[3,7,3]]))
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
