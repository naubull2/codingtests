# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A valid number can be split up into these components (in order):

	A decimal number or an integer.
	(Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

	(Optional) A sign character (either '+' or '-').
	One of the following formats:

		One or more digits, followed by a dot '.'.
		One or more digits, followed by a dot '.', followed by one or more digits.
		A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):

	(Optional) A sign character (either '+' or '-').
	One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false

Constraints:

	1 <= s.length <= 20
	s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""
import pytest


class Solution:
    def isNumber(self, s: str) -> bool:
        """Draw out a finite-state-machine(automaton)
        Then iterate throught the string -> just like a regex resolver
        """
        fsm = {
            0: {'digit': 2, 'sign': 1, 'dot': 3},
            1: {'digit': 2, 'dot': 3},
            2: {'digit': 2, 'dot': 4, 'exp': 5},
            3: {'digit': 4},
            4: {'digit': 4, 'exp': 5},
            5: {'sign': 6, 'digit': 7},
            6: {'digit': 7},
            7: {'digit': 7}
        }
        curr = 0
        for c in s:
            if c.isdigit():
                move = 'digit'
            elif c in ['+', '-']:
                move = 'sign'
            elif c.lower() == 'e':
                move = 'exp'
            elif c == '.':
                move = 'dot'
            else:
                return False  # non-valid char
            if move not in fsm[curr]:
                return False # no edge for such move

            curr = fsm[curr][move]
        return curr in [2, 4, 7]



@pytest.mark.parametrize('s, valid', [
    ("2", True),
    ("0089", True),
    ("-0.1", True),
    ("+3.14", True),
    ("4.", True),
    ("2e10", True),
    ("-90E3", True),
    ("3e+7", True),
    ("-123.456e789", True),
    ("abc", False),
    ("1e", False),
    ("e3", False)
])
def test(s, valid):
    assert valid == Solution().isNumber(s)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
