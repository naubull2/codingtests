# coding: utf-8
# Copyright © 2023 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	-105 <= Node.val <= 105
"""
from math import inf
import pytest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def build_tree(lst, constructor=TreeNode):
    # receive list as a binary tree, construct a tree return the root node pointer
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
        cur = (cur + 1) % 2
    return root
     

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        last_level = 1
        queue = deque([(root, 1)])
            
        level_sum = 0
        max_sum = -inf 
        ans = 1
        while queue:
            node, level = queue.popleft()

            if level > last_level:
                if level_sum > max_sum:
                    max_sum = level_sum
                    ans = level-1
                level_sum = 0

            level_sum += node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            last_level = level

        if level_sum > max_sum:
            return last_level
        return ans


@pytest.mark.parametrize('tree, expected', [
    ([1,7,0,7,-8,None,None], 2),
    ([-100,-200,-300,-20,-10,-5,None], 3)
])
def test(tree, expected):
    head = build_tree(tree)
    assert Solution().maxLevelSum(head) == expected
