# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

Constraints:

	1 <= n <= 2000
	0 <= dislikes.length <= 104
	dislikes[i].length == 2
	1 <= dislikes[i][j] <= n
	ai < bi
	All the pairs of dislikes are unique.
"""
import pytest
from typing import List
from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        labels = [-1] * (n+1) # we need 1-n
        # build an adjacency list from dislikes-edges
        adj = defaultdict(list)
        for s, t in dislikes:
            adj[s].append(t)
            adj[t].append(s)                

        def bfs(root):
            queue = deque([root])
            labels[root] = 0 # startwith 0, alternate on each level
            while queue:
                curr_node = queue.popleft()
                for neighbor in adj[curr_node]:
                    if labels[neighbor] == labels[curr_node]:
                        return False
                    elif labels[neighbor] == -1: # new node
                        labels[neighbor] = (labels[curr_node] + 1) % 2
                        queue.append(neighbor)
            return True
        
        for i in range(1, n+1):
            if labels[i] == -1:
                if not bfs(i):
                    return False
        return True


@pytest.mark.parametrize('n, edges, result', [
    (4, [[1,2],[1,3],[2,4]], True),
    (3, [[1,2],[1,3],[2,3]], False),
    (5, [[1,2],[2,3],[3,4],[4,5],[1,5]], False),
])
def test(n, edges, result):
    assert Solution().possibleBipartition(n, edges) == result

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
