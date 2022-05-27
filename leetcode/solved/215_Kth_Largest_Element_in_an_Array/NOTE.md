# Notes on Success
+ Since we don't need all elements but only Top-K elements in order,
  don't sort, but keep K elements in a min-heap to maintain the
  "running top-K", on reaching the end of the array, we have k-th largest
  at heap[0]

> Time : O(NlogK) , Space : O(K)
