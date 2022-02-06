### [1039. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge)

Easy

In a town, there are `` n `` people labeled from `` 1 `` to `` n ``. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1.   The town judge trusts nobody.
2.   Everybody (except for the town judge) trusts the town judge.
3.   There is exactly one person that satisfies properties __1__ and __2__.

You are given an array `` trust `` where <code>trust[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> representing that the person labeled <code>a<sub>i</sub></code> trusts the person labeled <code>b<sub>i</sub></code>.

Return _the label of the town judge if the town judge exists and can be identified, or return _`` -1 ``_ otherwise_.

 

__Example 1:__

```
Input: n = 2, trust = [[1,2]]
Output: 2
```

__Example 2:__

```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

__Example 3:__

```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

 

__Constraints:__

*   `` 1 <= n <= 1000 ``
*   <code>0 <= trust.length <= 10<sup>4</sup></code>
*   `` trust[i].length == 2 ``
*   All the pairs of `` trust `` are __unique__.
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   <code>1 <= a<sub>i</sub>, b<sub>i</sub> <= n</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 510,984 | 255,629 | 50.0% |