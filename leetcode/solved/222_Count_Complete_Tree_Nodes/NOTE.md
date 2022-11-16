# Notes on Success
+ A simple approach would be to BFS/DFS -> traversing all nodes,
  counting 1 for each node.
  ex)
  def dfs(root):
    return 1 + dfs(root.left) + dfs(root.right) if root else 0 

  But since we know the tree is a complete binary tree, we can expect at least 
   one of the left/right subtree must be a full tree.
  -> by checking logN down left, right and seeing if the depth is the same.
  -> if same, the tree at current node as root must be a full tree.
     where we know the full tree's node is at total = 2**H-1
  
  At a glance, this seem like O(1/2N) ~ O(N),
  we are using 2-pointer approach,
    one left, one right
    each will travel down exactly logN nodes.
     at each node, we run another O(logN) traverse down, for checking l.depth == r.depth
    so it is O(logN*logN) which is less than O(N)

> Time : O(logNxlogN) , Space : O(1)
