# Notes on Success
+ Using a hash map of counts, we count for each points i, j
  (where i < j) compute their gradient(slope) respect to point i.
  For the inner loop, we don't loop over all points but just
  points j > i, to avoid counting duplicates.
  
+ To further understand why its's a duplicate, for points i > j,
  we already checked that line between i,j is not the
  maximum (or eventually the maximum) when j was the pivot point.

> Time : O(n^2) , Space : O(n)
