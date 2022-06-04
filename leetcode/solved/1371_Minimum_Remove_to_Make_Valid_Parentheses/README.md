### [1371. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

Medium

Given a string 

<font face="monospace">s</font>

 of `` '(' `` , `` ')' `` and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `` '(' `` or `` ')' ``, in any positions ) so that the resulting _parentheses string_ is valid and return __any__ valid string.

Formally, a _parentheses string_ is valid if and only if:

*   It is the empty string, contains only lowercase characters, or
*   It can be written as `` AB `` (`` A `` concatenated with `` B ``), where `` A `` and `` B `` are valid strings, or
*   It can be written as `` (A) ``, where `` A `` is a valid string.

 

__Example 1:__

```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

__Example 2:__

```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

__Example 3:__

```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s[i] `` is either`` '(' `` , `` ')' ``, or lowercase English letter`` . ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 658,301 | 432,419 | 65.7% |