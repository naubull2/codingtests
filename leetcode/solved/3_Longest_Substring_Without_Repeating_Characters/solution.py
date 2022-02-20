# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

	0 <= s.length <= 5 * 104
	s consists of English letters, digits, symbols and spaces.
"""
import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keep a maximum sliding window of non-repeating chars
        maxLen = 0
        char2idx = dict()
        # [i, j] - if [i, j] has a repeating char, slide window to the position after the
        # repeating char
        i = 0
        for j in range(len(s)):
            if s[j] in char2idx:
                i = max(i, char2idx[s[j]]+1)
            maxLen = max(maxLen, j-i+1)
            char2idx[s[j]] = j
        return maxLen



@pytest.mark.parametrize('s, n', [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3)
])
def test(s, n):
    assert Solution().lengthOfLongestSubstring(s) == n

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
