# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Constraints:

	1 <= n <= 2 * 104
	edges.length == n - 1
	0 <= ai, bi < n
	ai != bi
	All the pairs (ai, bi) are distinct.
	The given input is guaranteed to be a tree and there will be no repeated edges.
"""
import pytest
import pdb
from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## O(n^2) solution will timeout.
        mht = []
        min_height = n

        tree = defaultdict(list)

        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
        for root in range(n):
            stack = [(root, -1, 0)]
            max_length = 0
            while stack:
                node, parent, height = stack.pop()
                max_length = max(height, max_length)
                # update stack, traverse through
                for c in tree[node]:
                    if c != parent:
                        stack.append((c, node, height+1))
            # reset on new mht
            if max_length < min_height:
                mht = [root]
                min_height = max_length
            elif max_length == min_height:
                mht.append(root)
        return mht
                
             


@pytest.mark.parametrize('n, edges, output', [
    (4, [[1,0],[1,2],[1,3]], [1]),
    (6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3, 4]),
    (8, [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]], [0])
])
def test(n, edges, output):
    assert Solution().findMinHeightTrees(n, edges) == output

if __name__ == '__main__':
    Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
