### [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)

Medium

Given the `` root `` of a binary tree, _determine if it is a valid binary search tree (BST)_.

A __valid BST__ is defined as follows:

*   The left subtree of a node contains only nodes with keys __less than__ the node's key.
*   The right subtree of a node contains only nodes with keys __greater than__ the node's key.
*   Both the left and right subtrees must also be binary search trees.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;"/>

```
Input: root = [2,1,3]
Output: true
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;"/>

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 4,571,361 | 1,397,329 | 30.6% |