# Notes on Success
+ runtime : 2260 ms (faster than 74% of python3 submissions)
+ memory : 75.1 MB (less than 71% of python3 submissions)

+ Single DFS through the graph while keeping track of discovery time and the lowest subtree connection of each node.
  This is a same problem as finding bridges in a network.
   - Tarjan's bridge finding algorithm will give us the critical connections, along with cycles.

> Time : O(E) , Space : O(V)
