### [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers)

Medium

You are given the `` root `` of a binary tree containing digits from `` 0 `` to `` 9 `` only.

Each root-to-leaf path in the tree represents a number.

*   For example, the root-to-leaf path `` 1 -> 2 -> 3 `` represents the number `` 123 ``.

Return _the total sum of all root-to-leaf numbers_. Test cases are generated so that the answer will fit in a __32-bit__ integer.

A __leaf__ node is a node with no children.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg" style="width: 212px; height: 182px;"/>

<strong>Input:</strong> root = [1,2,3]
    <strong>Output:</strong> 25
    <strong>Explanation:</strong>
    The root-to-leaf path 1->2 represents the number <code>12</code>.
    The root-to-leaf path <code>1->3</code> represents the number <code>13</code>.
    Therefore, sum = 12 + 13 = <code>25</code>.

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg" style="width: 292px; height: 302px;"/>

<strong>Input:</strong> root = [4,9,0,5,1]
    <strong>Output:</strong> 1026
    <strong>Explanation:</strong>
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path <code>4->9->1</code> represents the number 491.
    The root-to-leaf path <code>4->0</code> represents the number 40.
    Therefore, sum = 495 + 491 + 40 = <code>1026</code>.

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 1000] ``.
*   `` 0 <= Node.val <= 9 ``
*   The depth of the tree will not exceed `` 10 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 822,062 | 472,533 | 57.5% |