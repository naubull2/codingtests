# Notes on Success
+ We keep a count table for char counts in s1,
  comparing sliding window of s2.
  when we meet a overcount, we start from the last offset of that character

  we keep at most 26(alphabet) sized arrays

> Time : O(l1+(l2-l1)) , Space : O(1)
