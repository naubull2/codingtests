# Notes on Success
+ using prefix sum (accumulated sum),
  we can get range sum of [i, ..j] = prefix[j] -prefix[i-1]

+ If we do it naive way, O(n^3) -> O(n^2) using prefixsum

+ We can improve this from observation,
  [.....   i ......j   ...]
   %k == 1   %k==0   
  if prefix[i] %k == m,
  and prefix[j] %k == m,
  then sum[i+1 ~ j] %k == 0
  We can use this observation to make a O(n) algorithm

> Time : O(n) , Space : O(k)
