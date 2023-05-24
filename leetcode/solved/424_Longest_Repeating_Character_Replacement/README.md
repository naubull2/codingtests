### [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)

Medium

You are given a string `` s `` and an integer `` k ``. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `` k `` times.

Return _the length of the longest substring containing the same letter you can get after performing the above operations_.

 

<strong class="example">Example 1:</strong>

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

<strong class="example">Example 2:</strong>

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s `` consists of only uppercase English letters.
*   `` 0 <= k <= s.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 872,914 | 454,799 | 52.1% |