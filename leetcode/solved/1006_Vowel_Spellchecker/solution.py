# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

    Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.

        Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
        Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
        Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"

    Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.

        Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
        Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
        Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)

In addition, the spell checker operates under the following precedence rules:

    When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
    When the query matches a word up to capitlization, you should return the first such match in the wordlist.
    When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
    If the query has no matches in the wordlist, you should return the empty string.

Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

Example 1:
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
Example 2:
Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]

Constraints:

    1 <= wordlist.length, queries.length <= 5000
    1 <= wordlist[i].length, queries[i].length <= 7
    wordlist[i] and queries[i] consist only of only English letters.
"""
import pytest
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        answer = []

        def mask_vowels(word):
            return "".join("*" if c in "aeiou" else c for c in word.lower())

        exact_set = set(wordlist)
        capital_map = dict()
        vowel_map = dict()

        for w in wordlist:
            capital_map.setdefault(w.lower(), w)
            vowel_map.setdefault(mask_vowels(w), w)

        for q in queries:
            # exact match first
            if q in exact_set:
                answer.append(q)
            else:
                match = capital_map.get(q.lower(), "")
                if match:
                    # next try the captialization
                    answer.append(match)
                else:
                    # finally vowel correction, otherwise return empty
                    match = vowel_map.get(mask_vowels(q), "")
                    answer.append(match)

        return answer


@pytest.mark.parametrize(
    "wordlist, queries, expected",
    [
        (
            ["KiTe", "kite", "hare", "Hare"],
            [
                "kite",
                "Kite",
                "KiTe",
                "Hare",
                "HARE",
                "Hear",
                "hear",
                "keti",
                "keet",
                "keto",
            ],
            ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"],
        ),
        (["yellow"], ["YellOw"], ["yellow"]),
    ],
)
def test(wordlist, queries, expected):
    assert Solution().spellchecker(wordlist, queries) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
