### [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)

Hard

Given an array of `` points `` where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the __X-Y__ plane, return _the maximum number of points that lie on the same straight line_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg" style="width: 300px; height: 294px;"/>

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg" style="width: 300px; height: 294px;"/>

```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
```

 

__Constraints:__

*   `` 1 <= points.length <= 300 ``
*   `` points[i].length == 2 ``
*   <code>-10<sup>4</sup> <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>4</sup></code>
*   All the `` points `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,315,093 | 327,164 | 24.9% |