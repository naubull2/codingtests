### [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary)

Medium

Given an array of strings `` words `` representing an English Dictionary, return _the longest word in_ `` words `` _that can be built one character at a time by other words in_ `` words ``.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

<strong class="example">Example 1:</strong>

```
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
```

<strong class="example">Example 2:</strong>

```
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
```

 

__Constraints:__

*   `` 1 <= words.length <= 1000 ``
*   `` 1 <= words[i].length <= 30 ``
*   `` words[i] `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 264,403 | 137,609 | 52.0% |