# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1

Constraints:

	The number of nodes in the tree is in the range [0, 5 * 104].
	0 <= Node.val <= 5 * 104
	The tree is guaranteed to be complete.
"""
import pytest
from typing import Optional
from collections import deque



#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(lst, constructor=TreeNode):
    if not lst:
        return None
    root = constructor(lst[0])
    queue = deque([root])
    att = ['left', 'right']
    cur = 0
    for x in lst[1:]:
        node = constructor(x) if x is not None else None
        setattr(queue[0], att[cur], node)
        if cur:
            queue.popleft()
        if node:
            queue.append(node)
        cur += 1
        cur %= 2
    return root


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = r = 1
        left = right = root
        while left := left.left:
            l += 1
        while right := right.right:
            r += 1

        if l == r:
            return 2**l-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


@pytest.mark.parametrize('tree, output', [
    ([1,2,3,4,5,6], 6),
    ([], 0),
    ([1], 1)
])
def test(tree, output):
    root = build_tree(tree)
    assert output == Solution().countNodes(root)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
