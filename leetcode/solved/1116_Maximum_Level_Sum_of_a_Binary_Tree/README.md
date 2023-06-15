### [1116. Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

Medium

Given the `` root `` of a binary tree, the level of its root is `` 1 ``, the level of its children is `` 2 ``, and so on.

Return the __smallest__ level `` x `` such that the sum of all the values of nodes at level `` x `` is __maximal__.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/03/capture.JPG" style="width: 200px; height: 175px;"/>

```
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
```

<strong class="example">Example 2:</strong>

```
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 258,241 | 174,735 | 67.7% |