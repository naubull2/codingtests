### [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: “The lowest common ancestor is defined between two nodes `` p `` and `` q `` as the lowest node in `` T `` that has both `` p `` and `` q `` as descendants (where we allow __a node to be a descendant of itself__).”

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;"/>

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;"/>

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

__Example 3:__

```
Input: root = [2,1], p = 2, q = 1
Output: 2
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.
*   <code>-10<sup>9</sup> <= Node.val <= 10<sup>9</sup></code>
*   All `` Node.val `` are __unique__.
*   `` p != q ``
*   `` p `` and `` q `` will exist in the BST.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,341,905 | 769,112 | 57.3% |