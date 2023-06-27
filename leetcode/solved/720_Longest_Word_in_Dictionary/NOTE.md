# Notes on Success
+ Original problem's input size is too small, we can simply do it with a hashset

+ If k becomes large enough, N grows large enough, 
  O(nk) hashset method can be slow so I threwin some sort-by-length,
  thus making the hashset building time faster.

+ Though it has some overheads, on larger inputs trie based solution may work better.
  - solution2.py
  - We need to sort the words, and store all characters of words in a trie.

> Time : O(nlogn) , Space : O(n)
