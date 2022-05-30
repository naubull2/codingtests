### [79. Word Search](https://leetcode.com/problems/word-search/)

Medium

Given an `` m x n `` grid of characters `` board `` and a string `` word ``, return `` true `` _if_ `` word `` _exists in the grid_.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;"/>

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;"/>

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;"/>

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

 

__Constraints:__

*   `` m == board.length ``
*   `` n = board[i].length ``
*   `` 1 <= m, n <= 6 ``
*   `` 1 <= word.length <= 15 ``
*   `` board `` and `` word `` consists of only lowercase and uppercase English letters.

 

__Follow up:__ Could you use search pruning to make your solution faster with a larger `` board ``?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,461,000 | 978,509 | 39.8% |