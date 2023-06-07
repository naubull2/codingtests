### [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)

Hard

You are given an array of `` k `` linked-lists `` lists ``, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._

 

<strong class="example">Example 1:</strong>

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

<strong class="example">Example 2:</strong>

```
Input: lists = []
Output: []
```

<strong class="example">Example 3:</strong>

```
Input: lists = [[]]
Output: []
```

 

__Constraints:__

*   `` k == lists.length ``
*   <code>0 <= k <= 10<sup>4</sup></code>
*   `` 0 <= lists[i].length <= 500 ``
*   <code>-10<sup>4</sup> <= lists[i][j] <= 10<sup>4</sup></code>
*   `` lists[i] `` is sorted in __ascending order__.
*   The sum of `` lists[i].length `` will not exceed <code>10<sup>4</sup></code>.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 3,286,422 | 1,647,304 | 50.1% |