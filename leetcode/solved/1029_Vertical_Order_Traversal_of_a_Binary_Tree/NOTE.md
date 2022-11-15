# Notes on Success
+ We need to put the colliding elements in sorted order(by node.val)
  so we use (col, row, val) as the key for sorting
   -> Keep a hash table  col: [(row, val), ...]
   -> sorted by col, then the arry, outputing only the value[1]

 Time
  O(nlogn) for sorting the resulting array
  O(n) for initially traversing the tree

 Space
  O(2n) space for keeping the nodes from traversing the tree

> Time : O(NlogN) , Space : O(N)
