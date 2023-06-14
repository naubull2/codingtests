### [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii)

Medium

Given a circular integer array `` nums `` (i.e., the next element of `` nums[nums.length - 1] `` is `` nums[0] ``), return _the __next greater number__ for every element in_ `` nums ``.

The __next greater number__ of a number `` x `` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `` -1 `` for this number.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 492,033 | 311,180 | 63.2% |