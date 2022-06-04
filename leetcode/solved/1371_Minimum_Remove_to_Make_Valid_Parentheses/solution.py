# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

	It is the empty string, contains only lowercase characters, or
	It can be written as AB (A concatenated with B), where A and B are valid strings, or
	It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:

	1 <= s.length <= 105
	s[i] is either'(' , ')', or lowercase English letter.
"""
import pytest


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Keeping error indexes to remove later
        - keep unopend closers right away
        - add right most unclosed openers later on
        
                l ) ( ) ( a (
        balance 0 -11 0 1 0 2  = remove 2 right most closers
        """
        openers = []  # a stack to keep track of the opner indexes left unclosed
        errs = [] # keep track of the index of unopened closers
        balance = 0 # keep track of the open/close balance open:+1, close:-1
        for i, ch in enumerate(s):
            if ch == '(':
                balance += 1
                openers.append(i)
            elif ch == ')':
                if not balance:
                    errs.append(i)
                else:
                    balance -= 1
        
        if balance:
            errs.extend(openers[-balance:])
        errs = set(errs)
        return ''.join([ch for i, ch in enumerate(s) if i not in errs])
    
        """
        Two pass removal move back & forth twice,
         removing unmatched ) on going -> 
         removing unmatched ( on going <-
        """
        def remove_unmatch(s, opener='(', closer=')'):
            res = []
            open_cnt = 0
            for ch in s:
                if ch == closer:
                    if not open_cnt:
                        continue
                    else:
                        open_cnt -= 1
                elif ch == opener:
                    open_cnt += 1
                res.append(ch)
            return res
                
        res = remove_unmatch(s) # O(n)
        res = remove_unmatch(res[::-1], opener=')', closer='(') # O(n)
        return ''.join(res[::-1]) # O(n)


@pytest.mark.parametrize('', [
])
def test():
    pass

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
