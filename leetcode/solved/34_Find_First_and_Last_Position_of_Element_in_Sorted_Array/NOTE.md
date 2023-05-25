# Notes on Success
+ runtime : 72 ms (faster than 99.20% of python3 submissions)
+ memory : 15.4 MB (less than 48.02% of python3 submissions)

+ First start with a plain binary search,
  then modify the part where we have found the target,
   so we further do the binary search until we find the left/right-most targets.

   Essentially we are doing 2 binary searches so the complexity is still O(logN)

+ We can actually improve this by a small margin by sharing the first binary search 
  and run further searching for the left / right boundaries,
  but for the sake of readability, I would just leave it as it is.

> Time : O(log N) , Space : O(1)
