# Notes on Success
+ Way too straight forward solution.
  Simply build two counters up / down,
  then iterate through locations, droping first, then picking up.
  Finally, check the validity of such schedule. 

  - caveat : sorting would require nlogn... so it's not really an O(N) solution

> Time : O(NlogN) , Space : O(N)
