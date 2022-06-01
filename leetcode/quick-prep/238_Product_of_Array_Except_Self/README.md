### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)

Medium

Given an integer array `` nums ``, return _an array_ `` answer `` _such that_ `` answer[i] `` _is equal to the product of all the elements of_ `` nums `` _except_ `` nums[i] ``.

The product of any prefix or suffix of `` nums `` is __guaranteed__ to fit in a __32-bit__ integer.

You must write an algorithm that runs in `` O(n) `` time and without using the division operation.

 

__Example 1:__

```Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

__Example 2:__

```Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

 

__Constraints:__

*   <code>2 <= nums.length <= 10<sup>5</sup></code>
*   `` -30 <= nums[i] <= 30 ``
*   The product of any prefix or suffix of `` nums `` is __guaranteed__ to fit in a __32-bit__ integer.

 

__Follow up:__ Can you solve the problem in `` O(1)  ``extra space complexity? (The output array __does not__ count as extra space for space complexity analysis.)

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,840,549 | 1,179,451 | 64.1% |