# Notes on Success
+ sort array O(NlogN), then
  for i < j < k, given i, O(N)
  slide j and k from each left / right end, increment/decrementing
  according to the diff from the target.
   O(N) => O(N*N)

> Time : O(N**2) , Space : O(1)
