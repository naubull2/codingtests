# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

	The number of nodes in the tree is in the range [0, 104].
	-100 <= Node.val <= 100
"""
import pytest
from typing import Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        if root is None:
            return level
        depths = deque([(root, 0)])
        while depths:
            node, level = depths.popleft()
            if node.left:
                depths.append((node.left, level+1))
            if node.right:
                depths.append((node.right, level+1))
        return level


@pytest.mark.parametrize('', [
])
def test():
    pass

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
