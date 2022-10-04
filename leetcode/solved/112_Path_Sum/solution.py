# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

	The number of nodes in the tree is in the range [0, 5000].
	-1000 <= Node.val <= 1000
	-1000 <= targetSum <= 1000
"""
import pytest
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


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


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 1. simple BFS: easy to implement, straight forward, 
        # lacks memory efficiency
        if not root:
            return False

        q = deque([(root, root.val)])
        while q:
            node, partial_sum = q.popleft()
            if not node.left and not node.right:
                if partial_sum == targetSum:
                    return True

            if node.left:
                q.append((node.left, partial_sum + node.left.val))
            if node.right:
                q.append((node.right, partial_sum + node.right.val))
        return False 

        # 2. Simple recursion: DFS, easy to implement,
        # quicker than BFS in complete trees (where all leaf nodes are at the same level
        #if not root:
        #    return False

        #if not(root.left or root.right):
        #    if root.val == targetSum:
        #        return True
        #
        #partial_sum = targetSum - root.val
        #return (
        #    self.hasPathSum(root.left, partial_sum) or
        #    self.hasPathSum(root.right, partial_sum)
        #)




if __name__ == '__main__':
    root = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    targetSum = 22
    print(Solution().hasPathSum(root, targetSum))
    #sys.exit(pytest.main(['-s', '-v'] + sys.argv))
