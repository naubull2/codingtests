### [456. 132 Pattern](https://leetcode.com/problems/132-pattern)

Medium

Given an array of `` n `` integers `` nums ``, a __132 pattern__ is a subsequence of three integers `` nums[i] ``, `` nums[j] `` and `` nums[k] `` such that `` i < j < k `` and `` nums[i] < nums[k] < nums[j] ``.

Return `` true ``_ if there is a __132 pattern__ in _`` nums ``_, otherwise, return _`` false ``_._

 

__Example 1:__

```
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
```

__Example 2:__

```
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
```

__Example 3:__

```
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>1 <= n <= 2 * 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 445,819 | 144,178 | 32.3% |