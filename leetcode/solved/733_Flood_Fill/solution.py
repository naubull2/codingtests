# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]

Constraints:

	m == image.length
	n == image[i].length
	1 <= m, n <= 50
	0 <= image[i][j], newColor < 216
	0 <= sr < m
	0 <= sc < n
"""
import pytest
from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # BFS using a deque
        N, M = len(image), len(image[0])
        adj = deque()
        color = image[sr][sc]
        if color == newColor:
            return image

        adj.append((sr,sc)) # insert pixel position as a tuple of indices
        while adj: # keep expanding until no pixels are left to fill
            x, y = adj.popleft()
            if image[x][y] == color: # prevent duplicates
                image[x][y] = newColor
                for p in [(x-1, y), (x+1, y), (x,y-1),(x,y+1)]:
                    if 0 <= p[0] < N and 0 <= p[1] < M and image[p[0]][p[1]] == color:
                        # valid range and the color is the same
                        adj.append(p)
        return image
                        

@pytest.mark.parametrize('image, sr, sc, color, output', [
    ([[0,0,0],[0,1,1]], 1, 1, 1, [[0,0,0],[0,1,1]])
])
def test(image, sr, sc, color, output):
    assert Solution().floodFill(image, sr, sc, color) == output

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))

