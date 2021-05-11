# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

	Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
	cur's original left subtree should be the left subtree of the new left subtree root.
	cur's original right subtree should be the right subtree of the new right subtree root.
	If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:

Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:

Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	The depth of the tree is in the range [1, 104].
	-100 <= Node.val <= 100
	-105 <= val <= 105
	1 <= depth <= the depth of tree + 1
"""
import pytest

from queue import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes):
    root = TreeNode(nodes[0])
    queue = [root]
    atts = ['left', 'right']
    cur = 0
    for x in nodes[1:]:
        node = TreeNode(x) if x is not None else None
        setattr(queue[0], atts[cur], node)

        if cur: # right child done
            queue.pop(0)

        if node:
            queue.append(node)
        
        cur += 1
        cur %= 2
    return root


def compare_tree(t1, t2):
    if t1 and t2:
        return (t1.val == t2.val and
                compare_tree(t1.left, t2.left) and
                compare_tree(t1.right, t2.right))
    elif not t1 and not t2:
        return True
    else:
        return False


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val=val, left=root)
            
        # Collect all nodes at depth-1, do a BFS using a queue
        front = deque()
        front.append(root)
        breadth = len(front)
        level = 1
        while level < depth-1:
            for _ in range(breadth):
                node = front.popleft()
                if node.left: front.append(node.left)
                if node.right: front.append(node.right)
            breadth = len(front)
            level += 1
            
        # now we have all depth-1 nodes in the queue
        for _ in range(len(front)):
            node = front.popleft()
            node.left = TreeNode(val=val, left=node.left)
            node.right = TreeNode(val=val, right=node.right)
        return root


@pytest.mark.parametrize('nodes, val, depth, expected', [
    ([4,2,6,3,1,5], 1, 2, [4,1,1,2,None,None,6,3,1,5]),
    ([4,2,None,3,1], 1, 3, [4,2,None,1,1,3,None,None,1])
])
def test(nodes, val, depth, expected):
    # build initial Tree
    root = build_tree(nodes)
    assert compare_tree(build_tree(expected), Solution().addOneRow(root, val, depth))


if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
