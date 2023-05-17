### [948. Sort an Array](https://leetcode.com/problems/sort-an-array/)

Medium

Given an array of integers `` nums ``, sort the array in ascending order and return it.

You must solve the problem __without using any built-in__ functions in `` O(nlog(n)) `` time complexity and with the smallest space complexity possible.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
```

<strong class="example">Example 2:</strong>

```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 5 * 10<sup>4</sup></code>
*   <code>-5 * 10<sup>4</sup> <= nums[i] <= 5 * 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 672,067 | 398,110 | 59.2% |