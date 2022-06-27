# Notes on Success
+ We enumerate all possible sequences using backtracking
  (damage & repair recursion scheme)

+ Prune out any definite invalid sequences

+ For the leaf nodes(base cases) check if left / right number of parentheses match
 
+ Exponential solution is acceptable because the n is bounded to be small enough (<=20)

> Time : O(2^n) , Space : O(n)
