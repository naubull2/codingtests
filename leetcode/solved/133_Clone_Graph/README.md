### [133. Clone Graph](https://leetcode.com/problems/clone-graph/)

Medium

Given a reference of a node in a __<a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a>__ undirected graph.

Return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank">__deep copy__</a> (clone) of the graph.

Each node in the graph contains a value (`` int ``) and a list (`` List[Node] ``) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

 

__Test case format:__

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `` val == 1 ``, the second node with `` val == 2 ``, and so on. The graph is represented in the test case using an adjacency list.

__An adjacency list__ is a collection of unordered __lists__ used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `` val = 1 ``. You must return the __copy of the given node__ as a reference to the cloned graph.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png" style="width: 454px; height: 500px;"/>

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/07/graph.png" style="width: 163px; height: 148px;"/>

```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

<strong class="example">Example 3:</strong>

```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

 

__Constraints:__

*   The number of nodes in the graph is in the range `` [0, 100] ``.
*   `` 1 <= Node.val <= 100 ``
*   `` Node.val `` is unique for each node.
*   There are no repeated edges and no self-loops in the graph.
*   The Graph is connected and all nodes can be visited starting from the given node.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,824,445 | 967,674 | 53.0% |