# Notes on Success
+ runtime : 680 ms (faster than 84.24% of python3 submissions)
+ memory : 25.9 MB (less than 88.58% of python3 submissions)

+ Reducing the bucket size of the inverted index.
 - May be we can try the prefix / suffix trie instead of the inverted index to further reduce memory usages.
   - but then we would have time complexity increase of up to O(W) where W is the maximum word length.
 - Time complexity is N^2 for at most N entries being in the suffix / prefix match bucket for set intersection operation.
   - The worst case would be to have all words having the same prefix and suffix but no duplicate entries are fond.

> Time : O(N^2) , Space : O(WN)
