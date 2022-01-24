### [368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/)

Medium

Given a set of __distinct__ positive integers `` nums ``, return the largest subset `` answer `` such that every pair `` (answer[i], answer[j]) `` of elements in this subset satisfies:

*   `` answer[i] % answer[j] == 0 ``, or
*   `` answer[j] % answer[i] == 0 ``

If there are multiple solutions, return any of them.

 

__Example 1:__

```
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
```

__Example 2:__

```
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
```

 

__Constraints:__

*   `` 1 <= nums.length <= 1000 ``
*   <code>1 <= nums[i] <= 2 * 10<sup>9</sup></code>
*   All the integers in `` nums `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 349,749 | 140,348 | 40.1% |