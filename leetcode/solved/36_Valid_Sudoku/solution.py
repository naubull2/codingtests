# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

	Each row must contain the digits 1-9 without repetition.
	Each column must contain the digits 1-9 without repetition.
	Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
	Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

	board.length == 9
	board[i].length == 9
	board[i][j] is a digit 1-9 or '.'.
"""
import pytest
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check 9 rows
        for row in board:
            check = [0] * 10
            for cell in [int(v) for v in row if v != "."]:
                if check[cell] == 1:
                    return False
                else:
                    check[cell] = 1
        # check 9 columns
        for col_i in range(9):
            check = [0] * 10
            for cell in [
                int(board[row_i][col_i])
                for row_i in range(9)
                if board[row_i][col_i] != "."
            ]:
                if check[cell] == 1:
                    return False
                else:
                    check[cell] = 1

        # check 9 sub-boxes
        # create a 3 x 3 loop where each slot will represent [0:3], [3:6], [6:9]
        sub_ranges = [(0, 3), (3, 6), (6, 9)]
        for row_range in sub_ranges:
            for col_range in sub_ranges:  # 9 sub boxes
                check = [0] * 10
                for row in range(*row_range):  # check sum within a sub box
                    for col in range(*col_range):
                        cell = board[row][col]
                        if cell == ".":
                            continue
                        else:
                            cell = int(cell)
                        if check[cell] == 1:
                            return False
                        else:
                            check[cell] = 1
        return True


@pytest.mark.parametrize(
    "board, isValid",
    [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ),
        (
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            False,
        ),
    ],
)
def test(board, isValid):
    assert Solution().isValidSudoku(board) == isValid


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
