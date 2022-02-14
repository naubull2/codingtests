# Notes on Success
+ Same old binary search, but different not-found resolution.
  Through observations, we can safely conclude that on not-found
  occasions, lower boundary index is the place to insert the target.

> Time : O(logN) , Space : O(1)
