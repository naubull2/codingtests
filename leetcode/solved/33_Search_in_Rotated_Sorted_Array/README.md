### [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)

Medium

There is an integer array `` nums `` sorted in ascending order (with __distinct__ values).

Prior to being passed to your function, `` nums `` is __possibly rotated__ at an unknown pivot index `` k `` (`` 1 <= k < nums.length ``) such that the resulting array is `` [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] `` (__0-indexed__). For example, `` [0,1,2,4,5,6,7] `` might be rotated at pivot index `` 3 `` and become `` [4,5,6,7,0,1,2] ``.

Given the array `` nums `` __after__ the possible rotation and an integer `` target ``, return _the index of _`` target ``_ if it is in _`` nums ``_, or _`` -1 ``_ if it is not in _`` nums ``.

You must write an algorithm with `` O(log n) `` runtime complexity.

 

__Example 1:__

```Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

__Example 2:__

```Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

__Example 3:__

```Input: nums = [1], target = 0
Output: -1
```

 

__Constraints:__

*   `` 1 <= nums.length <= 5000 ``
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   All values of `` nums `` are __unique__.
*   `` nums `` is an ascending array that is possibly rotated.
*   <code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 3,823,797 | 1,443,594 | 37.8% |