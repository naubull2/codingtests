# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

import pytest


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        non-adjacent, non-empty meaning -> no numbers in a row
         -> at least one non-substitute must come after a substitution.
         -> we know the number sequence is done when we see another alpha, or end of string

        * word: Lower cases only
        * abbr: Lower cases + numbers
        * no integer overflows (32bit)

        2 pointers for word-i, abbr-j
        scan through the strings, check for failures

        # Test
        a -> a     : True
        gba -> 2a  : True
        gba  2a02  : False on leading zero
        a.aa -> 12 : True
        gba -> g2  :
         i=3   j=2


        >> PSEUDO CODE
        if len(abbr) > len(word): return False

        i, j, curr_num = 0, 0, 0
        while i < len(word) and j < len(abbr):
            if digit
                -> Fail if digit has leading 0
                -> update curr_num
                j++
            if char
                -> advance curr_num amount, then reset curr_num = 0
                -> Fail on out of bound or mismatch
                i++, j++
        if curr_num:
           -> handle remaining runs

        return i == len(word) and j == len(abbr)
        """
        if len(abbr) > len(word):
            return False

        i, j, curr_num = 0, 0, 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if curr_num == 0 and abbr[j] == "0":
                    return False
                curr_num = 10 * curr_num + int(abbr[j])
                j += 1

            elif abbr[j].isalpha():
                i += curr_num
                curr_num = 0

                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        if curr_num:
            i += curr_num

        return i == len(word) and j == len(abbr)


@pytest.mark.parametrize("word, abbr, result", [
    ('substitution', 's10n', True),
    ('a', 'a', True),
    ('gba', '2a', True),
    ('gba', '2a02', False),
    ('aaaaaaaaaaaa', '12', True),
    ('gba', 'g2', True)
])
def test(word, abbr, result):
    assert Solution().validWordAbbreviation(word, abbr) == result


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
