### [901. Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle)

Medium

Given two arrays `` nums1 `` and `` nums2 `` of equal size, the _advantage of `` nums1 `` with respect to `` nums2 ``_ is the number of indices `` i `` for which `` nums1[i] > nums2[i] ``.

Return __any__ permutation of `` nums1 `` that maximizes its advantage with respect to `` nums2 ``.

 

<div>
<p><strong>Example 1:</strong></p>
```
Input: nums1 = <span id="example-input-1-1">[2,7,11,15]</span>, nums2 = <span id="example-input-1-2">[1,10,4,11]</span>
Output: <span id="example-output-1">[2,11,7,15]</span>
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: nums1 = <span id="example-input-2-1">[12,24,8,32]</span>, nums2 = <span id="example-input-2-2">[13,25,32,11]</span>
Output: <span id="example-output-2">[24,32,8,12]</span>
```
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 <= nums1.length = nums2.length <= 10000</code></li>
<li><code>0 <= nums1[i] <= 10<sup>9</sup></code></li>
<li><code>0 <= nums2[i] <= 10<sup>9</sup></code></li>
</ol>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 89,473 | 45,399 | 50.7% |