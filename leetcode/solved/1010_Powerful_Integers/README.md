### [1010. Powerful Integers](https://leetcode.com/problems/powerful-integers/)

Medium

Given three integers `` x ``, `` y ``, and `` bound ``, return _a list of all the __powerful integers__ that have a value less than or equal to_ `` bound ``.

An integer is __powerful__ if it can be represented as <code>x<sup>i</sup> + y<sup>j</sup></code> for some integers `` i >= 0 `` and `` j >= 0 ``.

You may return the answer in __any order__. In your answer, each value should occur __at most once__.

 

__Example 1:__

```
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2<sup>0</sup> + 3<sup>0</sup>
3 = 2<sup>1</sup> + 3<sup>0</sup>
4 = 2<sup>0</sup> + 3<sup>1</sup>
5 = 2<sup>1</sup> + 3<sup>1</sup>
7 = 2<sup>2</sup> + 3<sup>1</sup>
9 = 2<sup>3</sup> + 3<sup>0</sup>
10 = 2<sup>0</sup> + 3<sup>2</sup>
```

__Example 2:__

```
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
```

 

__Constraints:__

*   `` 1 <= x, y <= 100 ``
*   <code>0 <= bound <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 97,297 | 42,193 | 43.4% |