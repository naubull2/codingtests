# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:

	1 <= s.length <= 3 * 105
	s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
	s represents a valid expression.
	All the integers in the expression are non-negative integers in the range [0, 231 - 1].
	The answer is guaranteed to fit in a 32-bit integer.
"""
import pytest


class Solution:
    def calculate(self, s: str) -> int:
        curr_num, op, buffer, result = 0, '+', 0, 0
        for c in s + '+':
            if c == ' ': continue
            if c.isdigit():
                curr_num = curr_num *10 + int(c)
                continue

            # handle last op: default to +
            if op == '+':
                result += buffer 
                buffer = curr_num

            elif op == '-':
                result += buffer
                buffer = -curr_num

            elif op == '*':
                buffer *= curr_num

            elif op == '/':
                buffer = buffer // curr_num if buffer > 0 else -(-buffer//curr_num)

            # reset curr_num and set next operator
            curr_num, op = 0, c

        # last operator is always + so simply add
        return result + buffer
                    
                    
        
@pytest.mark.parametrize('expr, result', [
    ('3+2*2', 7),
    ('3/2', 1),
    ('1-3/2', 0),
    ('1', 1),
    ('3+5/2', 5)
])
def test(expr, result):
    assert result == Solution().calculate(expr)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
