# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

Constraints:

	1 <= s.length <= 105
	s consists of lowercase English letters.
"""
import pytest

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        we have
        [a b c] mismatch! remove a -> bc, remove c -> ab
        [a a b]          remove a -> ab, remove b -> aa
        After removing either one, then if the rest of the string is palindrome
        it's a palindrome
        Checking palindrome is O(N)
        we test palindrom twice -> O(N)
        """
        def is_palind(st):
            n = len(st)
            for i in range(n//2):
                if st[i] != st[n-i-1]:
                    return False
            return True
        
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return is_palind(s[l+1:r+1]) or is_palind(s[l:r])
            else:
                l+=1
                r-=1
        return True
                

@pytest.mark.parametrize('s, output', [
    ('abc', False),
    ('aab', True),
    ('abcdba', True)
])
def test(s, output):
    assert Solution().validPalindrome(s) == output

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
