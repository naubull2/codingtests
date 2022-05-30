# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

	m == board.length
	n = board[i].length
	1 <= m, n <= 6
	1 <= word.length <= 15
	board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
import pytest


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        ROW, COL = len(board), len(board[0])
        path = set()

        
        # If no possible word can be found
        if n > ROW*COL:
            return False

        board_cnt = Counter(sum(board, []))
        for c, count in Counter(word).items():
            if board_cnt[c] < count:
                return False

        # start from word[0], word[-1] whose character is less frequent in the board
        if board_cnt[word[0]] > board_cnt[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if ( min(r, c) < 0 or r > ROW-1 or c > COL-1
              or (r, c) in path or board[r][c] != word[i]
            ):
                return False

            path.add((r, c))
            res = (dfs(r+1, c, i+1)
                or dfs(r, c+1, i+1)
                or dfs(r-1, c, i+1)
                or dfs(r, c-1, i+1)
            )
            path.remove((r, c))
            return res

        for i in range(ROW):
            for j in range(COL):
                if dfs(i, j, 0):
                    return True
        return False
        


@pytest.mark.parametrize('', [
])
def test():
    pass

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
