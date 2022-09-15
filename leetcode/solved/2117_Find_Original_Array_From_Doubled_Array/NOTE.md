# Notes on Success

+ Simplest approach would be to sort the array, then iterate through
  -> O(NlogN)

+ On many duplicates, sorting only on the keys(unique) would improve time
  -> O(N + klogk), still need O(N) for counting frequencies 

+ Then we get the 98% on time complexity.

> Time : O(N + klogk) , Space : O(N)
