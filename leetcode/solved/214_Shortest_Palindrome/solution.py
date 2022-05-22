# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:
Input: s = "abcd"
Output: "dcbabcd"

Constraints:

	0 <= s.length <= 5 * 104
	s consists of lowercase English letters only.
"""
import pytest


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ## check palindrome in k//2 comparison
        #def isPalindrome(st):
        #    if st[:len(st)//2] == st[::-1][:len(st)//2]:
        #        return True
        #    return False
    
        #for i in range(len(s), 0, -1):
        #    if isPalindrome(s[:i]):
        #        return s[i:][::-1] + s
        #return s[::-1] + s
        lsp = 0
        s1 = s
        s2 = s[::-1]
        while s1:
            if s1 == s2:
                lsp = len(s1)
                break
            s1 = s1[:-1]
            s2 = s2[1:]
        return s[lsp:][::-1] + s
        

@pytest.mark.parametrize('st, target', [
    ('aacecaaa', 'aaacecaaa'),
    ('abcd', 'dcbabcd'),
    ('aababa', 'ababaababa')
])
def test(st, target):
    assert Solution().shortestPalindrome(st) == target

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
