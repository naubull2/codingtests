### [816. Design HashSet](https://leetcode.com/problems/design-hashset/)

Easy

Design a HashSet without using any built-in hash table libraries.

Implement `` MyHashSet `` class:

*   `` void add(key) `` Inserts the value `` key `` into the HashSet.
*   `` bool contains(key) `` Returns whether the value `` key `` exists in the HashSet or not.
*   `` void remove(key) `` Removes the value `` key `` in the HashSet. If `` key `` does not exist in the HashSet, do nothing.

 

__Example 1:__

```
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)```

 

__Constraints:__

*   <code>0 <= key <= 10<sup>6</sup></code>
*   At most <code>10<sup>4</sup></code> calls will be made to `` add ``, `` remove ``, and `` contains ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 340,804 | 226,546 | 66.5% |
