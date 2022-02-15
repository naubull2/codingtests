### [189. Rotate Array](https://leetcode.com/problems/rotate-array)

Medium

Given an array, rotate the array to the right by `` k `` steps, where `` k `` is non-negative.

 

__Example 1:__

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

__Example 2:__

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>
*   <code>0 <= k <= 10<sup>5</sup></code>

 

__Follow up:__

*   Try to come up with as many solutions as you can. There are at least __three__ different ways to solve this problem.
*   Could you do it in-place with `` O(1) `` extra space?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,625,392 | 1,004,958 | 38.3% |