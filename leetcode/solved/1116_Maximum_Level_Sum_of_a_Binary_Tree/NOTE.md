# Notes on Success
+ We can collect <-level_sum, level> then sort and get the first level.
 - Even though D = logN so,
   O(DlogD) + O(N) = O(N)

+ We can even remove the sorting, by keep tracking of the maximum level sum.
  Only update when the maximum is exceeded.

+ Since we want minimum level, BFS seem more like a natural approach

> Time : O(N) , Space : O(N)
