# Notes on Success
+ First we scan the tree DFS until p and q are both found.
  While traversing we build a parent pointer using a hashmap.
  - DFS works better than BFS except for the worst case where p, q are
    left and right most leaf nodes where BFS == DFS, but other than this,
    DFS will terminate faster than BFS.

+ Once we found p and q,
  traverse from p to root, building path hashset
  then from q to root, traverse until a common node is found. 

> Time : O(N) , Space : O(N)
