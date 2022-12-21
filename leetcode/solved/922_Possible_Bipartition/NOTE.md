# Notes on Success
+ Nodes may not neccesarily in a single graph, but in multiple connected components
  (multi-graph situations)

  - keep a list of nodes and their labels,
  - BFS/DFS over the graph (dislike connection)
    - alternate labels are applied for neighbor nodes,
      - return False on meeting adjcent nodes with the same label.
        (contradicts the condition)

+ Traversing entire N nodes and E edges would take O(N+E) time and 
  having to store the edges and the nodes (adjacency list),
   O(N+E) space complexity as well

> Time : O(N+E) , Space : O(N+E)
