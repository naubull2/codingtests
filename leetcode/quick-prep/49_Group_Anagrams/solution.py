# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

	1 <= strs.length <= 104
	0 <= strs[i].length <= 100
	strs[i] consists of lowercase English letters.
"""
import pytest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def gen_key(st):
            return "".join(sorted(st))

        groups = dict()
        for s in strs:
            key = gen_key(s)
            groups.setdefault(key, []).append(s)
        return groups.values()


@pytest.mark.parametrize("", [])
def test():
    pass


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
