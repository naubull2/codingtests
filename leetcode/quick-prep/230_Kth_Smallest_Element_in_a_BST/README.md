### [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Medium

Given the `` root `` of a binary search tree, and an integer `` k ``, return _the_ <code>k<sup>th</sup></code> _smallest value (__1-indexed__) of all the values of the nodes in the tree_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;"/>

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;"/>

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

 

__Constraints:__

*   The number of nodes in the tree is `` n ``.
*   <code>1 <= k <= n <= 10<sup>4</sup></code>
*   <code>0 <= Node.val <= 10<sup>4</sup></code>

 

__Follow up:__ If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,176,652 | 796,441 | 67.7% |