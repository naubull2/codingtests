from tree import build_tree, TreeNode, serialize_tree

# invert given binary tree

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

print(serialize_tree(root))
invertTree(root)
print(serialize_tree(root))
