# Notes on Success
+ Start with simple approach, improve on the idea.

Simple: for range(i, j) we have substring s[i:j+1],
  check if s[i:j+1] can be converted to mono-char-string.
   - if s[i:j+1]'s non-most frequent chars is less than k, True
   - else, False
  if not try another substring

we need a frequency counter table, uppercase letters only = 26
-> constant space

instead of double for-loops, we can use sliding window with
two pointers l, r
move r each step, move l on failure.
-> linear time

> Time : O(N) , Space : O(1)
