### [99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree)

Medium

You are given the `` root `` of a binary search tree (BST), where the values of __exactly__ two nodes of the tree were swapped by mistake. _Recover the tree without changing its structure_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg" style="width: 422px; height: 302px;"/>

```
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg" style="width: 581px; height: 302px;"/>

```
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [2, 1000] ``.
*   <code>-2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1</code>

 
__Follow up:__ A solution using `` O(n) `` space is pretty straight-forward. Could you devise a constant `` O(1) `` space solution?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 665,506 | 324,344 | 48.7% |