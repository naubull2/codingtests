### [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node)

Medium

You are given a __perfect binary tree__ where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `` NULL ``.

Initially, all next pointers are set to `` NULL ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/14/116_sample.png" style="width: 500px; height: 171px;"/>

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

__Example 2:__

```
Input: root = []
Output: []
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 2<sup>12</sup> - 1]</code>.
*   `` -1000 <= Node.val <= 1000 ``

 

__Follow-up:__

*   You may only use constant extra space.
*   The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,214,671 | 675,704 | 55.6% |