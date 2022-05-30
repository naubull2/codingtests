# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.
"""
import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        opener = "({["
        closer = ")}]"
        stack = []
        for c in s:
            if c in opener:
                stack.append(c)
            else:
                if not stack:
                    return False  # No opener at all

                last = stack.pop()
                if closer[opener.index(last)] != c:  # Not a match
                    return False
        if stack:  # Any non-closed parenthesis
            return False
        return True


@pytest.mark.parametrize(
    "s, output",
    [("()", True), ("()[]{}", True), ("(]", False), ("(", False), ("]", False)],
)
def test(s, output):
    assert Solution().isValid(s) == output


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
