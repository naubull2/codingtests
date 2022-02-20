### [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)

Medium

Given a __1-indexed__ array of integers `` numbers `` that is already ___sorted in non-decreasing order___, find two numbers such that they add up to a specific `` target `` number. Let these two numbers be <code>numbers[index<sub>1</sub>]</code> and <code>numbers[index<sub>2</sub>]</code> where <code>1 <= index<sub>1</sub> < index<sub>2</sub> <= numbers.length</code>.

Return_ the indices of the two numbers, _<code>index<sub>1</sub></code>_ and _<code>index<sub>2</sub></code>_, __added by one__ as an integer array _<code>[index<sub>1</sub>, index<sub>2</sub>]</code>_ of length 2._

The tests are generated such that there is __exactly one solution__. You __may not__ use the same element twice.

Your solution must use only constant extra space.

 

__Example 1:__

```
Input: numbers = [<u>2</u>,<u>7</u>,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].
```

__Example 2:__

```
Input: numbers = [<u>2</u>,3,<u>4</u>], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 3. We return [1, 3].
```

__Example 3:__

```
Input: numbers = [<u>-1</u>,<u>0</u>], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].
```

 

__Constraints:__

*   <code>2 <= numbers.length <= 3 * 10<sup>4</sup></code>
*   `` -1000 <= numbers[i] <= 1000 ``
*   `` numbers `` is sorted in __non-decreasing order__.
*   `` -1000 <= target <= 1000 ``
*   The tests are generated such that there is __exactly one solution__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,476,038 | 859,520 | 58.2% |