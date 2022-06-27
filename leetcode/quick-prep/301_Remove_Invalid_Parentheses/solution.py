# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

Constraints:

	1 <= s.length <= 25
	s consists of lowercase English letters and parentheses '(' and ')'.
	There will be at most 20 parentheses in s.
"""
import pytest
from typing import List


class Solution:
    def reset(self, s):
        self.ans = set()
        self.s = s
        self.min_remove = float("inf")
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.reset(s)
        self.dfs(0, 0, 0, [], 0)
        
        return list(self.ans) # turn hashset to a list
    
    
    def dfs(self, i:int, num_left:int, num_right:int, expr:list, num_removed:int):
        
        # when we reach the end, determine if we want to keep it or not
        if i == len(self.s):
            if num_removed <= self.min_remove and num_left == num_right:
                if num_removed < self.min_remove:
                    self.ans = set() # recollect
                    self.min_remove = num_removed
                self.ans.add("".join(expr))
        else:
            if self.s[i] not in {'(', ')'}:
                expr.append(self.s[i])
                self.dfs(i+1, num_left, num_right, expr, num_removed)
                expr.pop()
            else:
                # remove current char
                self.dfs(i+1, num_left, num_right, expr, num_removed+1)

                # keep current char
                # keep only if not a definite invalid
                expr.append(self.s[i])
                if self.s[i] == '(':
                    self.dfs(i+1, num_left+1, num_right, expr, num_removed)
                elif self.s[i] == ')' and num_left > num_right:
                    # if there's at least one left parenthesis to match this
                    self.dfs(i+1, num_left, num_right+1, expr, num_removed)

                expr.pop()



@pytest.mark.parametrize('input, output', [
    ("()())()", ["(())()","()()()"]),
    ("(a)())()", ["(a())()","(a)()()"]),
    (")(", [""])
])
def test(input, output):
    assert set(Solution().removeInvalidParentheses(input)) == set(output)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
