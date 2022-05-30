# Notes on Success
+ Simply check if p, q exsits in the same subtree
  -> then we go deeper,
  -> otherwise (p == current, q==current, or a split)
    return current node, as LCA

> Time : O(logN) , Space : O(1)
