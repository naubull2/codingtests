# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

	The number of nodes in the tree is n.
	1 <= k <= n <= 104
	0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
import pytest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(lst, constructor=TreeNode):
    if not lst:
        return None
    root = constructor(lst[0])
    queue = [root]
    att = ["left", "right"]
    cur = 0
    for x in lst[1:]:
        node = constructor(x) if x is not None else None
        setattr(queue[0], att[cur], node)
        if cur:
            queue.pop(0)
        if node:
            queue.append(node)
        cur += 1
        cur %= 2
    return root


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                k -= 1
                if not k:
                    return current.val
                current = current.right
            else:
                break


@pytest.mark.parametrize(
    "values, k, expected",
    [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
        (
            [
                31,
                30,
                48,
                3,
                None,
                38,
                49,
                0,
                16,
                35,
                47,
                None,
                None,
                None,
                2,
                15,
                27,
                33,
                37,
                39,
                None,
                1,
                None,
                5,
                None,
                22,
                28,
                32,
                34,
                36,
                None,
                None,
                43,
                None,
                None,
                4,
                11,
                19,
                23,
                None,
                29,
                None,
                None,
                None,
                None,
                None,
                None,
                40,
                46,
                None,
                None,
                7,
                14,
                17,
                21,
                None,
                26,
                None,
                None,
                None,
                41,
                44,
                None,
                6,
                10,
                13,
                None,
                None,
                18,
                20,
                None,
                25,
                None,
                None,
                42,
                None,
                45,
                None,
                None,
                8,
                None,
                12,
                None,
                None,
                None,
                None,
                None,
                24,
                None,
                None,
                None,
                None,
                None,
                None,
                9,
            ],
            1,
            0,
        ),
    ],
)
def test(values, k, expected):
    root = build_tree(values)
    assert expected == Solution().kthSmallest(root, k)


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
