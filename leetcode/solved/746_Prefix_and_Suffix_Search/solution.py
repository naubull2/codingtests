# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

	WordFilter(string[] words) Initializes the object with the words in the dictionary.
	f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

Constraints:

	1 <= words.length <= 15000
	1 <= words[i].length <= 10
	1 <= prefix.length, suffix.length <= 10
	words[i], prefix and suffix consist of lower-case English letters only.
	At most 15000 calls will be made to the function f.
"""
import pytest
from typing import List
from collections import Counter

# The key is to reduce the bucket size so the set intersection wouldn't be costly.
class WordFilter:
    def __init__(self, words: List[str]):
        # Optimize by keeping the max idx for duplicates
        cnt = Counter(words)
        for i, w in enumerate(words):
            if cnt[w] > 1:
                cnt[w] -= 1
                words[i] = ""
            else:
                continue

        self.ivt_prefix = dict()
        self.ivt_suffix = dict()
        for w_i, w in enumerate(words):
            if w:
                for i in range(1, len(w) + 1):
                    self.ivt_prefix.setdefault(w[:i], set()).add(w_i)
                    self.ivt_suffix.setdefault(w[-i:], set()).add(w_i)

    def f(self, prefix: str, suffix: str) -> int:
        prefix_match = self.ivt_prefix.get(prefix, set())
        suffix_match = self.ivt_suffix.get(suffix, set())
        joint = prefix_match & suffix_match
        return max(joint)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


@pytest.mark.parametrize(
    "commands, args, expected",
    [
        (["WordFilter", "f"], [[["apple"]], ["a", "e"]], [None, 0]),
        (
            ["WordFilter", "f"],
            [[["a", "a", "a", "a", "a", "b", "b", "b", "b", "b"]], ["a", "a"]],
            [None, 4],
        ),
    ],
)
def test(commands, args, expected):
    o = globals()[commands[0]](*args[0])
    for cmd, arg, exp in zip(commands[1:], args[1:], expected[1:]):
        assert exp == getattr(o, cmd)(*arg)


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
