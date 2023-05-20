### [6. Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)

Medium

The string `` "PAYPALISHIRING" `` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `` "PAHNAPLSIIGYIR" ``

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

 

<strong class="example">Example 1:</strong>

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

<strong class="example">Example 2:</strong>

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

<strong class="example">Example 3:</strong>

```
Input: s = "A", numRows = 1
Output: "A"
```

 

__Constraints:__

*   `` 1 <= s.length <= 1000 ``
*   `` s `` consists of English letters (lower-case and upper-case), `` ',' `` and `` '.' ``.
*   `` 1 <= numRows <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,278,584 | 1,027,252 | 45.1% |