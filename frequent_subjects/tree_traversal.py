import pdb
from collections import deque

from tree import TreeNode, build_tree, print_tree, serialize_tree

# build a sample tree
root = build_tree([3, 1, 7, -3, 2, 4, 9])
print_tree(root)

###################
# DFS using a stack
###################
print("DFS")
stack = []  # to go down the tree and backtrack up
current = root

while stack or current:
    # Finish when nothing to go down or backtrack
    while current:
        # go down until left most leafnode
        stack.append(current)
        current = current.left

    current = stack.pop()
    print(current.val)
    current = current.right
        
    


###################
# BFS using a queue
###################
print("BFS")
q = deque([root])
while q:
    node = q.popleft()
    print(node.val)
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)
