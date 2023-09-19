# Notes on Success

+ We keep words in a trie, search starts at each cell i,j in the board.
  On reaching the terminal node(finding a word) prune the word from the trie
  for avoiding duplicate search later on in the search.
 

> Time : O(knm) , Space : O(n+m)
