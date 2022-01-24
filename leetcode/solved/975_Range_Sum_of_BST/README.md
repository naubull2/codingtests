### [975. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

Easy

Given the `` root `` node of a binary search tree and two integers `` low `` and `` high ``, return _the sum of values of all nodes with a value in the __inclusive__ range _`` [low, high] ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg" style="width: 400px; height: 222px;"/>

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg" style="width: 400px; height: 335px;"/>

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 2 * 10<sup>4</sup>]</code>.
*   <code>1 <= Node.val <= 10<sup>5</sup></code>
*   <code>1 <= low <= high <= 10<sup>5</sup></code>
*   All `` Node.val `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 642,865 | 544,582 | 84.7% |