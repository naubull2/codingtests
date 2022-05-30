# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:

	1 <= s.length <= 12
	s consists of lowercase English letters, uppercase English letters, and digits.
"""
import pytest
import pdb
from typing import List
from collections import deque


class Solution:
    # Permutation using iterative calls
    # def letterCasePermutation(self, s: str) -> List[str]:
    #    # It's a permutation problem so there's no other way, but to enumerate all cases.
    #    # so it should run in O(2^N) no matter what.
    #    # so the point here is to reduce the usage of memory
    #    # 1. recursive function
    #    result = deque([s])
    #    for i in range(len(s)):
    #        n = len(result)
    #        for j in range(n):
    #            string = result.popleft()
    #            result.extend(self.permute(string, i))
    #    return result
    #
    # def permute(self, string, offset):
    #    """Make a permutation of string at offset"""
    #    ch = string[offset]
    #    try:
    #        int(ch)
    #    except:
    #        return [f'{string[:offset]}{ch.lower()}{string[offset+1:]}',
    #                f'{string[:offset]}{ch.upper()}{string[offset+1:]}']
    #    else:
    #        return [string]

    # Permutation using recursive calls
    # def letterCasePermutation(self, s: str) -> List[str]:
    #    return [''.join(l) for l in self.permute([[]], s, 0)]
    #
    # def permute(self, cand, s, i):
    #    result = []
    #    if i >= len(s):
    #        return cand
    #    c = s[i]
    #    try:
    #        int(c)
    #    except:
    #        # char
    #        for l in cand:
    #            result.extend(self.permute([l+[c.upper()]], s, i+1))
    #            result.extend(self.permute([l+[c.lower()]], s, i+1))
    #    else:
    #        # int bypass
    #        for l in cand:
    #            result.extend(self.permute([l+[c]], s, i+1))
    #    return result

    # stack iteration with one function call
    def letterCasePermutation(self, s: str) -> List[str]:
        result = deque([[]])
        for ch in s:
            n = len(result)
            for i in range(n):
                candidate = result.popleft()
                if ch.isalpha():
                    result.append(candidate + [ch.swapcase()])
                result.append(candidate + [ch])

        return ["".join(l) for l in result]


@pytest.mark.parametrize(
    "string, output",
    [
        ("a1b2", ["a1b2", "a1B2", "A1b2", "A1B2"]),
        ("abc", ["abc", "Abc", "aBc", "abC", "ABc", "aBC", "AbC", "ABC"]),
    ],
)
def test(string, output):
    assert sorted(Solution().letterCasePermutation(string)) == sorted(output)


if __name__ == "__main__":
    print(Solution().letterCasePermutation("a1b2"))
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
