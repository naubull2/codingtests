# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:

	The number of nodes in the tree is in the range [1, 2 * 104].
	1 <= Node.val <= 105
	1 <= low <= high <= 105
	All Node.val are unique.
"""
import pytest
import pdb
from typing import Optional


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compose_bst(vals):
    def build_subtree_at(index, arr):
        if index > len(arr):
            return None
        node = TreeNode(arr[index-1])
        node.left = build_subtree_at(index*2, arr)
        node.right = build_subtree_at(index*2+1, arr)
        return node
    return build_subtree_at(1, vals)
                            

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, result = [root], 0
        while stack:
            node = stack.pop()
            if node is None or node.val is None:
                continue
            if node.val < low:
                stack.append(node.right)
            elif node.val <= high:
                stack.append(node.left)
                stack.append(node.right)
                result += node.val
            else:
                stack.append(node.left)
        return result


@pytest.mark.parametrize('root, low, high, expected', [
    ([10,5,15,3,7,13,18,1,None,6], 6, 10, 23),
    ([10,5,15,3,7,None,18], 7, 15, 32)
])
def test(root, low, high, expected):
    root = compose_bst(root)
    assert expected == Solution().rangeSumBST(root, low, high)


if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
