# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
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
import pytest
import pdb
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        """
        
        def intertwine(ws, sps):
            # one word + one sps appended
            t = []
            for w, s in zip(ws, sps):
                t.extend([w, s])
            t.append(ws[-1])
            return ''.join(t)
        
        
        # 1. Greedy pick words for each line
        cur_count = 0
        buffer = []
        lines = []
        for w in words:
            if (cur_count + len(w) + (1 if cur_count else 0)) <= maxWidth:
                cur_count += len(w) + (1 if cur_count else 0)
            else:
                lines.append(buffer)
                cur_count = len(w)
                buffer = []
            buffer.append(w)
        if buffer:
            lines.append(buffer)
        
        # 2. Justify spaces using divmod
        for i in range(len(lines)):
            remaining = maxWidth - (sum(len(w)+1 for w in lines[i]) - 1)
            
            # Left justify last line
            if i == len(lines)-1:
                lines[i] = ' '.join(lines[i]) + ' '*remaining
                
            # Full justify
            else:
                if len(lines[i]) > 1:
                    interval, left = divmod(remaining, len(lines[i])-1)
                    spaces = [' ' *(1+interval+ (1 if j < left else 0)) for j, w in enumerate(lines[i])][:-1]
                    lines[i] = intertwine(lines[i], spaces)
                else:
                    # Left justfiy if only 1 word per line
                    lines[i] = ' '.join(lines[i]) + ' '*remaining
        
        return lines
            
            
        
         

@pytest.mark.parametrize('input, length, output', [
    (["This", "is", "an", "example", "of", "text", "justification."],16,["This    is    an", "example  of text", "justification.  "]),
    (["Listen","to","many,","speak","to","a","few."], 6,["Listen","to    ","many  ,","speak ","to   a","few.  "])
])
def test(input, length, output):
    Solution().fullJustify(input, length) == output

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
