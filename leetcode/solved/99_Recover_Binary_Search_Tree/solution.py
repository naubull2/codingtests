# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:

	The number of nodes in the tree is in the range [2, 1000].
	-231 <= Node.val <= 231 - 1

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
"""
import pytest
import sys
from pathlib import Path

sys.path.append(str(Path("__file__").absolute().parent.parent.parent))
from tree import TreeNode, build_tree, serialize_tree
from typing import Optional


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Find two nodes while inorder traversing
        # mark each "wrongly-positioned" nodes
        # then on finding two nodes, swap them and exit

        # Time: O(N), Space: O(N)
        stack = []
        curr = root
        prev = None
        cand1, cand2 = None, None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if not cand1 and prev and prev.val > curr.val:
                # current val is off-place
                cand1, cand2 = prev, curr
            elif cand1 and prev.val > curr.val:
                # second off-place
                cand2 = curr
                break
            prev = curr
            curr = curr.right
        cand1.val, cand2.val = cand2.val, cand1.val
        return


@pytest.mark.parametrize(
    "tree, expected ",
    [
        ([3, 1, 4, None, None, 2], [2, 1, 4, None, None, 3]),
        ([1, 3, None, None, 2], [3, 1, None, None, 2]),
    ],
)
def test(tree, expected):
    input_tree = build_tree(tree)
    Solution().recoverTree(input_tree)
    assert serialize_tree(input_tree) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
