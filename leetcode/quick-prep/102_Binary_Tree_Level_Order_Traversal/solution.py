# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 2000].
	-1000 <= Node.val <= 1000
"""
import sys
import pytest
from typing import Optional, List
from collections import deque


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(lst):
    # given a list, build a binary tree
    # this already is a BFS-building
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    att = ['left', 'right']
    cur = 0 # we will swap this 0<->1 backnforth to access the atts
    for x in lst[1:]:
        node = TreeNode(x) if x is not None else None
        setattr(queue[0], att[cur], node)
        if cur: # right
            queue.popleft()
        if node: # expand
            queue.append(node)
        cur += 1
        cur %= 2
    return root


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)]) # node and its depth
        ans = [[]] # initialize with depth 0
        while q:
            node, depth = q.popleft()
            # do nothing if the node is None
            if node:
                if depth >= len(ans):
                    ans.append([]) # add new level when needed
            
                ans[depth].append(node.val)
                q.extend([(node.left, depth+1), (node.right, depth+1)])
        return ans
            


@pytest.mark.parametrize('tree, levels', [
    ([3,9,20,None,None,15,7], [[3], [9,20], [15,7]]),
    ([1], [[1]]),
    ([], [])
])
def test(tree, levels):
    root = build_tree(tree)
    assert Solution().levelOrder(root) == levels

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
