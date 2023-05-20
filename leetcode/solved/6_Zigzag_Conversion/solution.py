# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

	1 <= s.length <= 1000
	s consists of English letters (lower-case and upper-case), ',' and '.'.
	1 <= numRows <= 1000
"""
import pytest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        0     6     12
        1   5 7   11
        2  4  8 10
        3     9
        """
        if numRows == 1: # base case
            return s
        ans = [] # put resulting answer sequence in order
        for i in range(numRows):
            pos = i # column origin
            while pos < len(s):
                ans.append(s[pos]) 
                if i not in {0, numRows-1}: # diagonal element
                    if (pos + 2*(numRows-1-i)) < len(s):
                        ans.append(s[pos + 2*(numRows-1-i)])
                pos += 2*(numRows-1)  # next column origin
        return ''.join(ans)



@pytest.mark.parametrize('s, N, result', [
    ("A", 1, "A"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")
])
def test(s, N, result):
    assert Solution().convert(s, N) == result

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
