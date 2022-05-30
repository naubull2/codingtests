# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:

	The number of nodes in the tree is in the range [2, 105].
	-109 <= Node.val <= 109
	All Node.val are unique.
	p != q
	p and q will exist in the BST.
"""
import pytest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # assume p and q must exist in the tree?
        # root will always be a common ancestor of any two nodes in the tree (except for the root it self)
        # a node and its child range is (-inf, inf) for root
        # root.left => (-inf, root.val) & root.right => (root.val, inf)
        
        # we traverse left / right choosing which ever will include both p and q's values.
        # These chain of nodes are all common ancestors of p and q
        # We keep going down until we find a node that doesn't have any child with such subtree value range.
        
        """
        # Check if all values are included in the range <l, r>
        def is_common(l, r, vals):
            if (all(v.val >= l for v in vals) 
              and all(v.val <= r for v in vals)):
                return True
            return False
        
        # Tree nodes up to pow(10, 5) => less than 20 levels in a tree
        def lca(node, l, r):
            # when node is a common ancestor
            if node.left and is_common(l, node.val-1, [p, q]):
                return lca(node.left, l, node.val-1)
            elif node.right and is_common(node.val+1, r, [p, q]):
                return lca(node.right, node.val+1, r)
            return node
        
        return lca(root, -inf, inf)
        """
        
        # Now turn this logic into a iteration instead
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val: # both in the right subtree
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val: # both in the left subtree
                curr = curr.left
            else:
                return curr
                

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
