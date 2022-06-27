### [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses)

Hard

Given a string `` s `` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return _all the possible results_. You may return the answer in __any order__.

 

__Example 1:__

```
Input: s = "()())()"
Output: ["(())()","()()()"]
```

__Example 2:__

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
```

__Example 3:__

```
Input: s = ")("
Output: [""]
```

 

__Constraints:__

*   `` 1 <= s.length <= 25 ``
*   `` s `` consists of lowercase English letters and parentheses `` '(' `` and `` ')' ``.
*   There will be at most `` 20 `` parentheses in `` s ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 756,161 | 354,841 | 46.9% |