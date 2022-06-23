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
        Keep errs index while scaning,
        Then remove all error chars in the end using a string builder

        - 1 pass: when we meet a ), we can tell if it's error or not.
                : when we meet a (, we can't tell until the scan is over. May match later on..
        - keep indices of all (
          keep count of N unclosed errors, then remove right most N openers after the scan
        """
        num_opened = 0  # increment on open, decrement on close > 0, then we know # unclosed
        err_idx = []
        openers = []
        for i, c in enumerate(s):
            if c == '(':
                openers.append(i)
                num_opened += 1
            elif c == ')':
                if num_opened == 0:
                    err_idx.append(i)
                else:
                    num_opened -= 1
        if num_opened:
            err_idx.extend(openers[-num_opened:])
        return ''.join([c for i, c in enumerate(s) if i not in set(err_idx)])
                    



@pytest.mark.parametrize('input, output', [
    ("lee(t(c)o)de)", "lee(t(c)o)de"),
    ("a)b(c)d", "ab(c)d"),
    ("))((", "")
])
def test(input, output):
    assert output == Solution().minRemoveToMakeValid(input)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
