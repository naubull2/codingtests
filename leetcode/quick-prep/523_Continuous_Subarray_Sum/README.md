### [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum)

Medium

Given an integer array `` nums `` and an integer `` k ``, return `` true `` _if _`` nums ``_ has a continuous subarray of size __at least two__ whose elements sum up to a multiple of_ `` k ``_, or _`` false ``_ otherwise_.

An integer `` x `` is a multiple of `` k `` if there exists an integer `` n `` such that `` x = n * k ``. `` 0 `` is __always__ a multiple of `` k ``.

 

__Example 1:__

```
Input: nums = [23,<u>2,4</u>,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
```

__Example 2:__

```
Input: nums = [<u>23,2,6,4,7</u>], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
```

__Example 3:__

```
Input: nums = [23,2,6,4,7], k = 13
Output: false
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>0 <= nums[i] <= 10<sup>9</sup></code>
*   <code>0 <= sum(nums[i]) <= 2<sup>31</sup> - 1</code>
*   <code>1 <= k <= 2<sup>31</sup> - 1</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,086,783 | 297,544 | 27.4% |