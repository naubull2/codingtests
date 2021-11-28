### [1300. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)

Hard

There are `` n `` servers numbered from `` 0 `` to `` n - 1 `` connected by undirected server-to-server `` connections `` forming a network where <code>connections[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> represents a connection between servers <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>. Any server can reach other servers directly or indirectly through the network.

A _critical connection_ is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png" style="width: 198px; height: 248px;"/>

```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
```

__Example 2:__

```
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
```

 

__Constraints:__

*   <code>2 <= n <= 10<sup>5</sup></code>
*   <code>n - 1 <= connections.length <= 10<sup>5</sup></code>
*   <code>0 <= a<sub>i</sub>, b<sub>i</sub> <= n - 1</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   There are no repeated connections.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 257,906 | 133,740 | 51.9% |