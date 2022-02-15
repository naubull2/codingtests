### [1019. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array)

Easy

Given an integer array `` nums `` sorted in __non-decreasing__ order, return _an array of __the squares of each number__ sorted in non-decreasing order_.

 

__Example 1:__

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

__Example 2:__

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

 

__Constraints:__

*   <code><span>1 <= nums.length <= </span>10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   `` nums `` is sorted in __non-decreasing__ order.

 
__Follow up:__ Squaring each element and sorting the new array is very trivial, could you find an `` O(n) `` solution using a different approach?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,191,695 | 852,486 | 71.5% |