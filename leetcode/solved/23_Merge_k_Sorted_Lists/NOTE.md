# Notes on Success
+  By keeping a minheap of size K, where K is the number of lists,
   we can keep adding the smallest of all K-lists's heads.

+ Take caution when moving around lists as they are only single directed,
  if no pointer is left behind, we can't reverse traverse the list.

> Time : O(NlogK) , Space : O(K)
