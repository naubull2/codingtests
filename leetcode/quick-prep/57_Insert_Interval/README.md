### [57. Insert Interval](https://leetcode.com/problems/insert-interval)

Medium

You are given an array of non-overlapping intervals `` intervals `` where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represent the start and the end of the <code>i<sup>th</sup></code> interval and `` intervals `` is sorted in ascending order by <code>start<sub>i</sub></code>. You are also given an interval `` newInterval = [start, end] `` that represents the start and end of another interval.

Insert `` newInterval `` into `` intervals `` such that `` intervals `` is still sorted in ascending order by <code>start<sub>i</sub></code> and `` intervals `` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `` intervals ``_ after the insertion_.

 

__Example 1:__

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

__Example 2:__

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

 

__Constraints:__

*   <code>0 <= intervals.length <= 10<sup>4</sup></code>
*   `` intervals[i].length == 2 ``
*   <code>0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10<sup>5</sup></code>
*   `` intervals `` is sorted by <code>start<sub>i</sub></code> in __ascending__ order.
*   `` newInterval.length == 2 ``
*   <code>0 <= start <= end <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,373,406 | 514,772 | 37.5% |