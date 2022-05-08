### [933. Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)

Easy

Given the `` root `` of a binary search tree, rearrange the tree in __in-order__ so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg" style="width: 600px; height: 350px;"/>

```
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg" style="width: 300px; height: 114px;"/>

```
Input: root = [5,1,7]
Output: [1,null,5,null,7]
```

 

__Constraints:__

*   The number of nodes in the given tree will be in the range `` [1, 100] ``.
*   `` 0 <= Node.val <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 271,402 | 212,473 | 78.3% |