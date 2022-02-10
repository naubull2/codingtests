### [382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node)

Medium

Given a singly linked list, return a random node's value from the linked list. Each node must have the __same probability__ of being chosen.

Implement the `` Solution `` class:

*   `` Solution(ListNode head) `` Initializes the object with the head of the singly-linked list `` head ``.
*   `` int getRandom() `` Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg" style="width: 302px; height: 62px;"/>

```
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
```

 

__Constraints:__

*   The number of nodes in the linked list will be in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code>
*   At most <code>10<sup>4</sup></code> calls will be made to `` getRandom ``.

 

__Follow up:__

*   What if the linked list is extremely large and its length is unknown to you?
*   Could you solve this efficiently without using extra space?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 250,599 | 147,121 | 58.7% |