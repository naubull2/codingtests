# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]

Constraints:

	2 <= n <= 105
	n - 1 <= connections.length <= 105
	0 <= ai, bi <= n - 1
	ai != bi
	There are no repeated connections.
"""
from typing import List
from collections import defaultdict
from math import inf

import pytest
import pdb


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        critical_connections = []
        if not connections:
            return [[]]

        # build graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * len(graph)  # Node's first discovery time
        low = [None] * len(graph)  # Node's lowest subtree

        def traverse_graph(node, parent, t):
            disc[node] = t
            low[node] = t

            t += 1
            for c in sorted(graph[node]):
                if disc[c] == -1:
                    traverse_graph(c, node, t)
                    t += 1
                    low[node] = min(low[c], low[node])
                elif c != parent:
                    low[node] = min(low[node], disc[c])
            if disc[parent] < low[node]:
                critical_connections.append([parent, node])

        parent = -1
        t = 0
        traverse_graph(0, parent, t)
        return critical_connections


@pytest.mark.parametrize(
    "network, expected",
    [
        ([[0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [5, 1]], [{0, 1}, {3, 4}]),
        ([[0, 1], [1, 2], [2, 0], [1, 3]], [{1, 3}]),
        ([[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [3, 5], [4, 5]], [{1, 3}]),
        ([[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5]], [{1, 3}, {3, 4}, {4, 5}]),
    ],
)
def test(network, expected):
    output = Solution().criticalConnections(len(network), network)
    result = []
    assert len(output) == len(expected)
    for pair in output:
        result.append(set(pair) in expected)
    assert all(result)


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
