# Notes on Success
+ min-access time == min-distance

  Dijkstra should come to mind
  - Finding the current min access time edge is found using minheap

  for each node V,
     find min-access time O(logV) (heappop)

  for all edge E, heappsh is called O(logV)

    so, O(VlogV + ElogV) = O((E+V)logV)

> Time : O((E+V)logV) , Space : O(V)
