### [2366. Maximum Bags With Full Capacity of Rocks](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks)

Medium

You have `` n `` bags numbered from `` 0 `` to `` n - 1 ``. You are given two __0-indexed__ integer arrays `` capacity `` and `` rocks ``. The <code>i<sup>th</sup></code> bag can hold a maximum of `` capacity[i] `` rocks and currently contains `` rocks[i] `` rocks. You are also given an integer `` additionalRocks ``, the number of additional rocks you can place in __any__ of the bags.

Return_ the __maximum__ number of bags that could have full capacity after placing the additional rocks in some bags._

 

<strong class="example">Example 1:</strong>

```
Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
Output: 3
Explanation:
Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.
```

<strong class="example">Example 2:</strong>

```
Input: capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
Output: 3
Explanation:
Place 8 rocks in bag 0 and 2 rocks in bag 2.
The number of rocks in each bag are now [10,2,2].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that we did not use all of the additional rocks.
```

 

__Constraints:__

*   `` n == capacity.length == rocks.length ``
*   <code>1 <= n <= 5 * 10<sup>4</sup></code>
*   <code>1 <= capacity[i] <= 10<sup>9</sup></code>
*   `` 0 <= rocks[i] <= capacity[i] ``
*   <code>1 <= additionalRocks <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 120,099 | 81,533 | 67.9% |