# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.
import pytest
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # preprocess (transposing words, so letters at k per each jth word in words)
        choices = [[w[i] for w in words] for i in range(len(words[0]))]

        def dfs(k, i, num_ways, build):
            if i >= len(target) or k >= len(choices):
                return num_ways if build == len(target) else 0

            num_with, num_without = 0, 0
            # num with k
            if target[i] in choices[k]:
                num_with = dfs(k+1, i+1,
                    (num_ways if num_ways else 1) * choices[k].count(target[i]),
                    build + 1
                )

            # num without k
            num_without = dfs(k+1, i, num_ways, build)
            print(f"{k}-{i}-{num_ways} = {num_with} + {num_without}")
            return num_with + num_without

        return dfs(0, 0, 0, 0)
            


@pytest.mark.parametrize("words, target, expected", [
    (["acca", "bbbb", "caca"], "aba", 6),
    (["abba", "baab"], "bab", 4),
    (["abcd"], "abcd", 1),
    (["acca", "bbbb", "caca"], "dba", 0)
])
def test(words, target, expected):
    assert Solution().numWays(words, target) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
