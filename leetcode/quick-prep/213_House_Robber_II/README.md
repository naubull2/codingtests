### [213. House Robber II](https://leetcode.com/problems/house-robber-ii)

Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are __arranged in a circle.__ That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and __it will automatically contact the police if two adjacent houses were broken into on the same night__.

Given an integer array `` nums `` representing the amount of money of each house, return _the maximum amount of money you can rob tonight __without alerting the police___.

 

__Example 1:__

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

__Example 2:__

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

__Example 3:__

```
Input: nums = [1,2,3]
Output: 3
```

 

__Constraints:__

*   `` 1 <= nums.length <= 100 ``
*   `` 0 <= nums[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,011,558 | 404,608 | 40.0% |