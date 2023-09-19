# coding: utf-8
# Copyright © 2023 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:

	m == board.length
	n == board[i].length
	1 <= m, n <= 12
	board[i][j] is a lowercase English letter.
	1 <= words.length <= 3 * 104
	1 <= words[i].length <= 10
	words[i] consists of lowercase English letters.
	All the strings of words are unique.
"""
import pytest


from functools import reduce


# traverse down the trie, removing the word
def prune(trie, word):
    t = trie
    nodes = []
    for c in word:
        if c not in t:
            return False
        t = t[c]
        # node pointer and the character
        nodes.append((t, c))
    if "$" in t:
        # on reaching the terminal node
        p = "$"
        # traverse bottom up(reverse)
        for node, c in nodes[::-1]:
            # remove only if no reference or terminal node
            # as other word may have the same prefix
            if len(node[p]) == 0 or p == "$":
                del node[p]
            p = c

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie containg all the words in word
        COLS, ROWS = len(board), len(board[0])

        # syntax sugar for recursive dict with empty dict as next node
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = "$"

        for word in words:
            reduce(dict.__getitem__, word, trie)[END] = word
        
        # helper for finding adjacent nodes
        def adj(x, y):
            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if 0 <= x+i < COLS and 0 <= y+j < ROWS:
                    yield (x+i, y+j)

        # prevent duplicates
        ans = set()
        # recursive search
        def DFS(i, j, node):
            if END in node:
                # word is stored in the terminal nodes
                ans.add(node[END])
                # remove found word for avoiding later duplicates
                prune(trie, node[END]) 

            # mark & unmark strategy
            # unmark after exploration
            letter = board[i][j]
            board[i][j] = ""
            for x, y in adj(i, j):
                if board[x][y] in node:
                    DFS(x, y, node[board[x][y]])
            board[i][j] = letter
            return
        
        for i in range(COLS):
            for j in range(ROWS):
                # check if there's any word that start with board[i][j]
                if board[i][j] in trie:
                    DFS(i, j, trie[board[i][j]])
        return ans
