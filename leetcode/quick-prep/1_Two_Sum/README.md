### [1. Two Sum](https://leetcode.com/problems/two-sum)

Easy

Given an array of integers `` nums `` and an integer `` target ``, return _indices of the two numbers such that they add up to `` target ``_.

You may assume that each input would have ___exactly_ one solution__, and you may not use the _same_ element twice.

You can return the answer in any order.

 

__Example 1:__

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

__Example 2:__

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

__Example 3:__

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

 

__Constraints:__

*   <code>2 <= nums.length <= 10<sup>4</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>
*   <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code>
*   __Only one valid answer exists.__

 
__Follow-up: __Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>) </code>time complexity?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 13,718,206 | 6,669,339 | 48.6% |