# Notes on Success
+ all permutation problems can only run in O(n^m) so the point would be to 
  reduce number of subcalls, or memory usages.
  I approached in 3 ways, settling with double ended queue BFS
  - reducing string concat operations to maximum, only concat at the very end.

> Time : O(2^N), Space : O(2^N)
