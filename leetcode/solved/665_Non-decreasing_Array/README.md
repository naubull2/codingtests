### [665. Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array)

Medium

Given an array `` nums `` with `` n `` integers, your task is to check if it could become non-decreasing by modifying __at most one element__.

We define an array is non-decreasing if `` nums[i] <= nums[i + 1] `` holds for every `` i `` (__0-based__) such that (`` 0 <= i <= n - 2 ``).

 

__Example 1:__

<strong>Input:</strong> nums = [4,2,3]
    <strong>Output:</strong> true
    <strong>Explanation:</strong> You could modify the first 4 to <code>1</code> to get a non-decreasing array.

__Example 2:__

```
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>1 <= n <= 10<sup>4</sup></code>
*   <code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 720,213 | 150,033 | 20.8% |