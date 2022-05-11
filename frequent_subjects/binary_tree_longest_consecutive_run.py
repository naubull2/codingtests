from tree import build_tree, TreeNode, serialize_tree
from collections import deque
# Given a binary tree, find the length of the longest consecutive sequence path.
# sequence is a path from root to the node (only top-down traverse)

# BFS
# Keep a separate storage for tracking each node's run-length

def longest_run(root: TreeNode) -> int:
    level = deque([root]) # BFS level traverse queue
    run_size = deque([1]) # root will have run size 1
    max_run = 1

    while level:
        node = level.popleft()
        run = run_size.popleft() # to keep them aligned must pop when node pops

        left_run, right_run = run, run 
        if node.left:
            if node.val == node.left.val-1:
                left_run += 1
                max_run = max(max_run, left_run)
            else:
                run = 1
            level.append(node.left)
            run_size.append(left_run)
        if node.right:
            if node.val == node.right.val-1:
                right_run += 1
                max_run = max(max_run, right_run)
            else:
                run = 1
            level.append(node.right)
            run_size.append(right_run)
    return max_run


root = build_tree([3, 2, 4, 4, 3, None, 5, None, None, None, 4, 6, 7, 1, 5])
print(longest_run(root))
             

root = build_tree([4, 2, 5, 1, None, 6])
print(longest_run(root))

# Or we can DFS -> where we build run from bottom-up
