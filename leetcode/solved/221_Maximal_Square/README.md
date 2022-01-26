### [221. Maximal Square](https://leetcode.com/problems/maximal-square)

Medium

Given an `` m x n `` binary `` matrix `` filled with `` 0 ``'s and `` 1 ``'s, _find the largest square containing only_ `` 1 ``'s _and return its area_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" style="width: 400px; height: 319px;"/>

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg" style="width: 165px; height: 165px;"/>

```
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

__Example 3:__

```
Input: matrix = [["0"]]
Output: 0
```

 

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 <= m, n <= 300 ``
*   `` matrix[i][j] `` is `` '0' `` or `` '1' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,065,638 | 455,856 | 42.8% |