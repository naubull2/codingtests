import pdb

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# build binary tree from a list
def build_tree(lst, constructor=TreeNode):
    if not lst:
        return None
    root = constructor(lst[0])
    queue = [root]
    att = ['left', 'right']
    cur = 0
    for x in lst[1:]:
        node = constructor(x) if x is not None else None
        setattr(queue[0], att[cur], node)
        if cur:
            queue.pop(0)
        if node:
            queue.append(node)
        cur = (cur + 1)%2
    return root

# serialize into an array
def serialize_tree(root):
    ret = []
    if not root:
        return ret
    level = [root]
    while level:
        new_level = []
        for node in level:
            if node is None:
                ret.append(node)
            else:
                if node:
                    ret.append(node.val)
                    new_level.append(node.left)
                    new_level.append(node.right)
        level = new_level
    while ret and ret[-1] is None:
        ret.pop()
    return ret
