### [222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

Medium

Given the `` root `` of a __complete__ binary tree, return the number of the nodes in the tree.

According to __<a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a>__, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `` 1 `` and <code>2<sup>h</sup></code> nodes inclusive at the last level `` h ``.

Design an algorithm that runs in less than <code data-stringify-type="code">O(n)</code> time complexity.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px;"/>

```
Input: root = [1,2,3,4,5,6]
Output: 6
```

<strong class="example">Example 2:</strong>

```
Input: root = []
Output: 0
```

<strong class="example">Example 3:</strong>

```
Input: root = [1]
Output: 1
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.
*   <code>0 <= Node.val <= 5 * 10<sup>4</sup></code>
*   The tree is guaranteed to be __complete__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 852,979 | 508,243 | 59.6% |