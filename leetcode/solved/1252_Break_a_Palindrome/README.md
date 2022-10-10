### [1252. Break a Palindrome](https://leetcode.com/problems/break-a-palindrome)

Medium

Given a palindromic string of lowercase English letters `` palindrome ``, replace __exactly one__ character with any lowercase English letter so that the resulting string is __not__ a palindrome and that it is the __lexicographically smallest__ one possible.

Return _the resulting string. If there is no way to replace a character to make it not a palindrome, return an __empty string__._

A string `` a `` is lexicographically smaller than a string `` b `` (of the same length) if in the first position where `` a `` and `` b `` differ, `` a `` has a character strictly smaller than the corresponding character in `` b ``. For example, `` "abcc" `` is lexicographically smaller than `` "abcd" `` because the first position they differ is at the fourth character, and `` 'c' `` is smaller than `` 'd' ``.

 

<strong class="example">Example 1:</strong>

```
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "<u>z</u>bccba", "a<u>a</u>ccba", and "ab<u>a</u>cba".
Of all the ways, "aaccba" is the lexicographically smallest.
```

<strong class="example">Example 2:</strong>

```
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
```

 

__Constraints:__

*   `` 1 <= palindrome.length <= 1000 ``
*   `` palindrome `` consists of only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 190,363 | 100,696 | 52.9% |