### [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

Medium

A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank">__trie__</a> (pronounced as "try") or __prefix tree__ is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

*   `` Trie() `` Initializes the trie object.
*   `` void insert(String word) `` Inserts the string `` word `` into the trie.
*   `` boolean search(String word) `` Returns `` true `` if the string `` word `` is in the trie (i.e., was inserted before), and `` false `` otherwise.
*   `` boolean startsWith(String prefix) `` Returns `` true `` if there is a previously inserted string `` word `` that has the prefix `` prefix ``, and `` false `` otherwise.

 

__Example 1:__

```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

 

__Constraints:__

*   `` 1 <= word.length, prefix.length <= 2000 ``
*   `` word `` and `` prefix `` consist only of lowercase English letters.
*   At most <code>3 * 10<sup>4</sup></code> calls __in total__ will be made to `` insert ``, `` search ``, and `` startsWith ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,008,338 | 590,241 | 58.5% |