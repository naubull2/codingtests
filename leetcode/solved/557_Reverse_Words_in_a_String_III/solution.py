# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:

	1 <= s.length <= 5 * 104
	s contains printable ASCII characters.
	s does not contain any leading or trailing spaces.
	There is at least one word in s.
	All the words in s are separated by a single space.
"""
import pytest


class Solution:
    def reverseWords(self, s: str) -> str:
        # direct manipulation using a stack
        """
        word = []
        output = []
        for c in list(s):
            if c != ' ':
                word.append(c)
            else:
                while word:
                    output.append(word.pop())
                output.append(c)
        while word:
            output.append(word.pop())
        return ''.join(output)
        """

        # Or just keep the index of a word's starting point only, then reverse the string
        output = []
        w_i = 0
        word = False
        for i, c in enumerate(s):
            if c != " ":
                if not word:
                    w_i = i
                    word = True
            else:
                if word:
                    # end of the word
                    output.append(s[w_i:i][::-1])
                output.append(c)
                word = False
        if word:
            output.append(s[w_i:][::-1])
        return "".join(output)


@pytest.mark.parametrize(
    "s, reversed", [("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc")]
)
def test(s, reversed):
    assert reversed == Solution().reverseWords(s)


if __name__ == "__main__":
    Solution().reverseWords("Let's take LeetCode contest")
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
