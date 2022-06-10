### [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii)

Medium

Given a string `` s `` which represents an expression, _evaluate this expression and return its value_. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>.

__Note:__ You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `` eval() ``.

 

__Example 1:__

```Input: s = "3+2*2"
Output: 7
```

__Example 2:__

```Input: s = " 3/2 "
Output: 1
```

__Example 3:__

```Input: s = " 3+5 / 2 "
Output: 5
```

 

__Constraints:__

*   <code>1 <= s.length <= 3 * 10<sup>5</sup></code>
*   `` s `` consists of integers and operators `` ('+', '-', '*', '/') `` separated by some number of spaces.
*   `` s `` represents __a valid expression__.
*   All the integers in the expression are non-negative integers in the range <code>[0, 2<sup>31</sup> - 1]</code>.
*   The answer is __guaranteed__ to fit in a __32-bit integer__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,046,380 | 436,550 | 41.7% |