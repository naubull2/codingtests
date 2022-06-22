### [65. Valid Number](https://leetcode.com/problems/valid-number/)

Hard

A __valid number__ can be split up into these components (in order):

1.   A __decimal number__ or an __integer__.
2.   (Optional) An `` 'e' `` or `` 'E' ``, followed by an __integer__.

A __decimal number__ can be split up into these components (in order):

1.   (Optional) A sign character (either `` '+' `` or `` '-' ``).
2.   One of the following formats:	
    
    1.   One or more digits, followed by a dot `` '.' ``.
    2.   One or more digits, followed by a dot `` '.' ``, followed by one or more digits.
    3.   A dot `` '.' ``, followed by one or more digits.
    
    
    

An __integer__ can be split up into these components (in order):

1.   (Optional) A sign character (either `` '+' `` or `` '-' ``).
2.   One or more digits.

For example, all the following are valid numbers: `` ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"] ``, while the following are not valid numbers: `` ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"] ``.

Given a string `` s ``, return `` true ``_ if _`` s ``_ is a __valid number___.

 

__Example 1:__

```
Input: s = "0"
Output: true
```

__Example 2:__

```
Input: s = "e"
Output: false
```

__Example 3:__

```
Input: s = "."
Output: false
```

 

__Constraints:__

*   `` 1 <= s.length <= 20 ``
*   `` s `` consists of only English letters (both uppercase and lowercase), digits (`` 0-9 ``), plus `` '+' ``, minus `` '-' ``, or dot `` '.' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,516,283 | 277,765 | 18.3% |