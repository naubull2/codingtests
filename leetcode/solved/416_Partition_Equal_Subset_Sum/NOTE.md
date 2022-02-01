# Notes on Success
+ Approx. split into two, then shift or swap at most N times to see if 
  target sum can be reached. At most N shift/exchange trials, conclude as False.
  - Though passed the online judge, I'm not entirely sure this holds true in all cases.

> Time : O(N) , Space : O(N) : a whooping 84.67% / 93.42% rank

+ Or we can reduce the problem into a knapsack problem(NP-complete),
  using a dynamic programming to solve it.
  - one partition would be the capacity, breaking down using a recurrence equation

> Time : O(logN), Space : O(N^2) : lack in space usage, though 78.30% / 12.31% rank
