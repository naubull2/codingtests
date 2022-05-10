# Notes on Success
+ We in-order traverse (if healthy BST, it should be sorted)
  - find first and second "out-of-place" nodes.
    A > B  : first is A
    C > D : second is D
  - then swap A and D 

+ At most we have to search the entire tree O(N)
  - stack can't be larger than N as for the skewed linear-chain looking tree

> Time : O(N) , Space : O(N)
