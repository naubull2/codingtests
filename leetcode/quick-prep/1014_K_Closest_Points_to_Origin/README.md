### [1014. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin)

Medium

Given an array of `` points `` where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the __X-Y__ plane and an integer `` k ``, return the `` k `` closest points to the origin `` (0, 0) ``.

The distance between two points on the __X-Y__ plane is the Euclidean distance (i.e., <code>√(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup></code>).

You may return the answer in __any order__. The answer is __guaranteed__ to be __unique__ (except for the order that it is in).

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg" style="width: 400px; height: 400px;"/>

```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

__Example 2:__

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

 

__Constraints:__

*   <code>1 <= k <= points.length <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> < x<sub>i</sub>, y<sub>i</sub> < 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,193,622 | 787,125 | 65.9% |