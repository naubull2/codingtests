### [200. Number of Islands](https://leetcode.com/problems/number-of-islands)

Medium

Given an `` m x n `` 2D binary grid `` grid `` which represents a map of `` '1' ``s (land) and `` '0' ``s (water), return _the number of islands_.

An __island__ is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

__Example 1:__

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

__Example 2:__

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m, n <= 300 ``
*   `` grid[i][j] `` is `` '0' `` or `` '1' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,932,381 | 1,588,985 | 54.2% |