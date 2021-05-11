# Notes on Success

+ runtime : 232 ms (faster than 89.76% of python3 submissions)
+ memory : 24.8 MB (less than 36.15% of python3 submissions)

+ On each checkouts we save the travel time of "id", keeping a list of all travels of the same source-destination pairs.

+ At most N/2 which is the entire travels, may start and end in the same courses 
  - So a summation of N/2 integers is the maximum operations

> Time : O(N) , Space : O(N)
