from tree import build_tree, TreeNode, serialize_tree
from collections import deque

# invert given binary tree in-place

root = build_tree([4, 2, 5, 1, None, 6])

def invertTree(root: TreeNode) -> None:
    # return if leaf node
    if root is None:
        return 
    # swap left and right subtrees
    root.right, root.left = root.left, root.right
    # recurse into left and right
    invertTree(root.left)
    invertTree(root.right)


def invertTree(root: TreeNode) -> None:
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            continue
        q.extend([node.left, node.right])
        node.left, node.right = node.right, node.left

print(serialize_tree(root))
invertTree(root)
print(serialize_tree(root))


