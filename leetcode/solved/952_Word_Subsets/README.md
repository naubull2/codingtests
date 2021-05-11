### [952. Word Subsets](https://leetcode.com/problems/word-subsets/)

Medium

We are given two arrays `` A `` and `` B `` of words.  Each word is a string of lowercase letters.

Now, say that word `` b `` is a subset of word `` a ``__ __if every letter in `` b `` occurs in `` a ``, __including multiplicity__.  For example, `` "wrr" `` is a subset of `` "warrior" ``, but is not a subset of `` "world" ``.

Now say a word `` a `` from `` A `` is _universal_ if for every `` b `` in `` B ``, `` b `` is a subset of `` a ``. 

Return a list of all universal words in `` A ``.  You can return the words in any order.

 

<div>
<p><strong>Example 1:</strong></p>
```
Input: A = <span id="example-input-1-1">["amazon","apple","facebook","google","leetcode"]</span>, B = <span id="example-input-1-2">["e","o"]</span>
Output: <span id="example-output-1">["facebook","google","leetcode"]</span>
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: A = <span id="example-input-2-1">["amazon","apple","facebook","google","leetcode"]</span>, B = <span id="example-input-2-2">["l","e"]</span>
Output: <span id="example-output-2">["apple","google","leetcode"]</span>
```
<div>
<p><strong>Example 3:</strong></p>
```
Input: A = <span id="example-input-3-1">["amazon","apple","facebook","google","leetcode"]</span>, B = <span id="example-input-3-2">["e","oo"]</span>
Output: <span id="example-output-3">["facebook","google"]</span>
```
<div>
<p><strong>Example 4:</strong></p>
```
Input: A = <span id="example-input-4-1">["amazon","apple","facebook","google","leetcode"]</span>, B = <span id="example-input-4-2">["lo","eo"]</span>
Output: <span id="example-output-4">["google","leetcode"]</span>
```
<div>
<p><strong>Example 5:</strong></p>
```
Input: A = <span id="example-input-5-1">["amazon","apple","facebook","google","leetcode"]</span>, B = <span id="example-input-5-2">["ec","oc","ceo"]</span>
Output: <span id="example-output-5">["facebook","leetcode"]</span>
```
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 <= A.length, B.length <= 10000</code></li>
<li><code>1 <= A[i].length, B[i].length <= 10</code></li>
<li><code>A[i]</code> and <code>B[i]</code> consist only of lowercase letters.</li>
<li>All words in <code>A[i]</code> are unique: there isn't <code>i != j</code> with <code>A[i] == A[j]</code>.</li>
</ol>
</div>
</div>
</div>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 82,854 | 43,704 | 52.7% |