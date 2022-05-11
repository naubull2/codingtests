# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	-231 <= Node.val <= 231 - 1
"""
import math
import sys
import pytest
from pathlib import Path
sys.path.append(str(Path('__file__').absolute().parent.parent.parent))
from tree import TreeNode, build_tree, serialize_tree
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursion
        def isRangeValidBST(node, low, high) -> bool:
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            
            return (isRangeValidBST(node.left, low, node.val) 
                    and isRangeValidBST(node.right, node.val, high))
    
        return isRangeValidBST(root, -math.inf, math.inf)

@pytest.mark.parametrize('tree, isvalid', [
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False)
])
def test(tree, isvalid):
    root = build_tree(tree)
    assert isvalid == Solution().isValidBST(root)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
