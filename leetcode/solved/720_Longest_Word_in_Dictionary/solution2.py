# coding: utf-8
# Copyright © 2023 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Constraints:

	1 <= words.length <= 1000
	1 <= words[i].length <= 30
	words[i] consists of lowercase English letters.
"""
import pytest
import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.val = ""

    def __le__(self, node):
        return self.val <= node.val

    def __lt__(self, node):
        return self.val < node.val

    def __ge__(self, node):
        return self.val >= node.val

    def __gt__(self, node):
        return self.val > node.val


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
        cur.val = word

    def bfs(self):
        q = collections.deque([self.root])
        ans = ""
        while q:
            cur = q.popleft()
            # sort each char for lexicographical sorting
            for child in sorted(cur.children.values()):
                if child.is_word:
                    q.append(child)
                    if len(child.val) > len(ans):
                        ans = child.val
                # any non-words can be ignored
        return ans


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # increasing size / lexicographical order
        trie = Trie()
        for w in words:
            trie.addWord(w)
        return trie.bfs()



@pytest.mark.parametrize('words, output', [
  (["a","banana","app","appl","ap","apply","apple"], "apple"),
  (["w", "wo", "wor", "worl", "world"], "world")
])
def test(words, output):
    assert Solution().longestWord(words) == output
