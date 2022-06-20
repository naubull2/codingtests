# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:

	1 <= k <= points.length <= 104
	-104 < xi, yi < 104
"""
import pytest
from queue import PriorityQueue
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        #1. Max-heap
        Oh yeah.. just using a maxheap to keep K-closest, scanning the array, should be fine. 
        O(nlogk) time complexity, O(k) space complexity
        
        #2. Any O(n)?
        - binary search? O(n)
        
        draw a circle of radius of R -> check how many points are within
         preprocess distance O(n)
        
        approximately search for the middle each time, 
        reducing half of the points each round.
        N + N/2 + N/4 + .....+ N/N = 2N
        """

        '''
        # Precompute the distance for each point
        def split_distances(remaining, distances, mid):
            closer, farther = [], []
            for index in remaining:
                if distances[index] <= mid:
                    closer.append(index)
                else:
                    farther.append(index)
            return [closer, farther]

        def distance(point):
            return point[0]**2 + point[1]**2

        distances = [distance(point) for point in points]
        remaining = [i for i in range(len(points))]
        # bsearch range
        low, high = 0, max(distances)
        
        # Perform a binary search of the distances
        # to find the k closest points
        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = split_distances(remaining, distances, mid)
            if len(closer) > k:
                # then discard the farther points and continue
                remaining = closer
                high = mid
            else:
                # Add the closer points to the answer array and keep
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low = mid
                
        return [points[i] for i in closest]
        '''
    
        # we are not sorting entire array but just keep top K elements
        # maybe we have duplicates, so keep 2K elements.
        topk = PriorityQueue()  # put / get
        for p in points: # O(n)
            distance = p[0]**2 + p[1]**2
            topk.put((-distance, p))  # max heap
            
            while topk.qsize() > k:  # O(logk) to pop one element, heapify again.
                _ = topk.get() # only k values are present in the heap
            
        # O(nlogk) total
        
        # we endup with less than or equal to k-points in topk
        ans = []
        while not topk.empty():
            ans.append(topk.get()[1])
        
        return ans     
    

        
        


@pytest.mark.parametrize('', [
])
def test():
    pass

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
