### [2117. Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array)

Medium

An integer array `` original `` is transformed into a __doubled__ array `` changed `` by appending __twice the value__ of every element in `` original ``, and then randomly __shuffling__ the resulting array.

Given an array `` changed ``, return `` original ``_ if _`` changed ``_ is a __doubled__ array. If _`` changed ``_ is not a __doubled__ array, return an empty array. The elements in_ `` original `` _may be returned in __any__ order_.

 

__Example 1:__

```
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
```

__Example 2:__

```
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
```

__Example 3:__

```
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
```

 

__Constraints:__

*   <code>1 <= changed.length <= 10<sup>5</sup></code>
*   <code>0 <= changed[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 215,133 | 87,556 | 40.7% |