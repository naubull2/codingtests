# Notes on Success
+ We can check for unopened closer on 1st pass,
  but can't detect unclosed opener on 1st pass, 
    as it may be closed later on.

+ keep all index of openers then later, remove N right most
  unclosed openers

+ total of 2-pass scan is needed

> Time : O(N) , Space : O(N)
