# Notes on Success
+ As we call next() N times, we visit nodes twice each. (stack in, stack out)
  So the amortized complexity would be O(N) for N calls, O(1) for a single call.
  - We keep at most (h-1) nodes in the backtrack stack. 

> Time : O(1) per call to next() , Space : O(h)
