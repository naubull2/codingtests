# Notes on Success
+ runtime : 72 ms (faster than 99.20% of python3 submissions)
+ memory : 15.4 MB (less than 48.02% of python3 submissions)

+ In place binary search down to the min-max range of the given target.
  - We divide process into two phases.
    1. First find if the target exists at all.
    2. If exists, then we binary search further into left and right partition of the found target index.
      - In the second phase of the binary search, we binary search until the last match in the given direction is found. 

> Time : O(log N) , Space : O(1)
