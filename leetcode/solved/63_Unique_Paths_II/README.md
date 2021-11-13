### [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii)

Medium

A robot is located at the top-left corner of a `` m x n `` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as `` 1 `` and `` 0 `` respectively in the grid.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" style="width: 242px; height: 242px;"/>

```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" style="width: 162px; height: 162px;"/>

```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

 

__Constraints:__

*   `` m == obstacleGrid.length ``
*   `` n == obstacleGrid[i].length ``
*   `` 1 <= m, n <= 100 ``
*   `` obstacleGrid[i][j] `` is `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,088,391 | 391,620 | 36.0% |