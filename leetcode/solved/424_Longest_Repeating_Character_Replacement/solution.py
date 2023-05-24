# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

Constraints:

	1 <= s.length <= 105
	s consists of only uppercase English letters.
	0 <= k <= s.length
"""
import pytest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        ans = 0
        # two pointers approach, l, r
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            if (r-l+1) - maxf > k: # not enough, skip to next range
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1) 
        return ans


@pytest.mark.parametrize('s, k, answer', [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4)
])
def test(s, k, answer):
    assert Solution().characterReplacement(s, k) == answer

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
