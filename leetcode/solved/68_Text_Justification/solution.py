# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

	A word is defined as a character sequence consisting of non-space characters only.
	Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
	The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:

	1 <= words.length <= 300
	1 <= words[i].length <= 20
	words[i] consists of only English letters and symbols.
	1 <= maxWidth <= 100
	words[i].length <= maxWidth
"""
import pdb
import sys
import pytest
from typing import List

from itertools import chain


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Cluster words per line first, without justifying
        lines, line = [], []
        line_width = 0
        for w in words:
            # handle overflow first
            if line_width + len(w) + (1 if line_width else 0) > maxWidth:
                lines.append(line)
                line, line_width = [], 0
            line_width += len(w) + (1 if line_width else 0)
            line.append(w)
        if line:
            lines.append(line)
        
        def fill_spaces(words, maxlen, isLeft=False):
            spaces = [1] * (len(words)-1)
            # compute spaces
            padding = maxlen - sum([len(w) for w in words]) - sum(spaces)
            if isLeft:
                spaces.append(padding)
            else:
                i = 0
                while padding: # round-robin distribution
                    spaces[i] += 1 
                    i += 1
                    i %= len(spaces)
                    padding -= 1
            # merge words and spaces
            if len(spaces) < len(words):
                spaces.append(0)
            spaces = [' ' * s for s in spaces]
            return ''.join(chain(*zip(words, spaces)))
        
        ans = []
        for i, l in enumerate(lines):
            is_left = False
            if len(l) == 1 or i == (len(lines)-1):
                is_left = True
            ans.append(fill_spaces(l, maxWidth, isLeft=is_left))
        return ans


@pytest.mark.parametrize('words, width, expected', [
 (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
   20,
   [
     "Science  is  what we",
     "understand      well",
     "enough to explain to",
     "a  computer.  Art is",
     "everything  else  we",
     "do                  "
   ]),
 (["Listen","to","many,","speak","to","a","few."],
   6,
  ["Listen", "to    ", "many, ", "speak ", "to   a", "few.  "])

])
def test(words, width, expected):
    assert Solution().fullJustify(words, width) == expected


if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
