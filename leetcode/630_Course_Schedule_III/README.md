### [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii)

Hard

There are `` n `` different online courses numbered from `` 1 `` to `` n ``. You are given an array `` courses `` where <code>courses[i] = [duration<sub>i</sub>, lastDay<sub>i</sub>]</code> indicate that the <code>i<sup>th</sup></code> course should be taken __continuously__ for <code>duration<sub>i</sub></code> days and must be finished before or on <code>lastDay<sub>i</sub></code>.

You will start on the <code>1<sup>st</sup></code> day and you cannot take two or more courses simultaneously.

Return _the maximum number of courses that you can take_.

 

__Example 1:__

```
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1<sup>st</sup> course, it costs 100 days so you will finish it on the 100<sup>th</sup> day, and ready to take the next course on the 101<sup>st</sup> day.
Second, take the 3<sup>rd</sup> course, it costs 1000 days so you will finish it on the 1100<sup>th</sup> day, and ready to take the next course on the 1101<sup>st</sup> day. 
Third, take the 2<sup>nd</sup> course, it costs 200 days so you will finish it on the 1300<sup>th</sup> day. 
The 4<sup>th</sup> course cannot be taken now, since you will finish it on the 3300<sup>th</sup> day, which exceeds the closed date.
```

__Example 2:__

```
Input: courses = [[1,2]]
Output: 1
```

__Example 3:__

```
Input: courses = [[3,2],[4,3]]
Output: 0
```

 

__Constraints:__

*   <code>1 <= courses.length <= 10<sup>4</sup></code>
*   <code>1 <= duration<sub>i</sub>, lastDay<sub>i</sub> <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 128,631 | 44,797 | 34.8% |