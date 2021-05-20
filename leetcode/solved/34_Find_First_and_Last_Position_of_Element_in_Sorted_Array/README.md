### [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Medium

Given an array of integers `` nums `` sorted in ascending order, find the starting and ending position of a given `` target `` value.

If `` target `` is not found in the array, return `` [-1, -1] ``.

You must write an algorithm with `` O(log n) `` runtime complexity.

 

__Example 1:__

```Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

__Example 2:__

```Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

__Example 3:__

```Input: nums = [], target = 0
Output: [-1,-1]
```

 

__Constraints:__

*   <code>0 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>
*   `` nums `` is a non-decreasing array.
*   <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,899,524 | 720,559 | 37.9% |