### [733. Flood Fill](https://leetcode.com/problems/flood-fill)

Easy

An image is represented by an `` m x n `` integer grid `` image `` where `` image[i][j] `` represents the pixel value of the image.

You are also given three integers `` sr ``, `` sc ``, and `` newColor ``. You should perform a __flood fill__ on the image starting from the pixel `` image[sr][sc] ``.

To perform a __flood fill__, consider the starting pixel, plus any pixels connected __4-directionally__ to the starting pixel of the same color as the starting pixel, plus any pixels connected __4-directionally__ to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `` newColor ``.

Return _the modified image after performing the flood fill_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg" style="width: 613px; height: 253px;"/>

```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
```

__Example 2:__

```
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
```

 

__Constraints:__

*   `` m == image.length ``
*   `` n == image[i].length ``
*   `` 1 <= m, n <= 50 ``
*   <code>0 <= image[i][j], newColor < 2<sup>16</sup></code>
*   `` 0 <= sr < m ``
*   `` 0 <= sc < n ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 614,241 | 354,511 | 57.7% |