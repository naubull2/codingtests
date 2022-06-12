### [55. Jump Game](https://leetcode.com/problems/jump-game)

Medium

You are given an integer array `` nums ``. You are initially positioned at the array's __first index__, and each element in the array represents your maximum jump length at that position.

Return `` true ``_ if you can reach the last index, or _`` false ``_ otherwise_.

 

__Example 1:__

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

__Example 2:__

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   <code>0 <= nums[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,713,693 | 1,030,209 | 38.0% |