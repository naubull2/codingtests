# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.
import pytest

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # encode with a meta information prefix: {size of string}+#+{string}
        return ''.join([f'{len(s)}#{s}' for s in strs])

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res


@pytest.mark.parametrize("input, output", [
    (["leet","code","love","you"],["leet","code","love","you"]),
    (["neet", "co#de", "ro:;cks"], ["neet", "co#de", "ro:;cks"])
])
def test(input, output):
    obj = Solution()
    assert obj.decode(obj.encode(input)) == output


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
