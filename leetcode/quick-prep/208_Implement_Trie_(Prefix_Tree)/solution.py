# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

	Trie() Initializes the trie object.
	void insert(String word) Inserts the string word into the trie.
	boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
	boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

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

Constraints:

	1 <= word.length, prefix.length <= 2000
	word and prefix consist only of lowercase English letters.
	At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
import pytest


''' Clarification
    insert("word")
    insert("war")
    insert("worm")
    represent Trie nodes by having attributes : value, and childs = dict()
                      "" = root 
    
               "w"
               
             "o"   "a"
                   
        "r"          "r"
        
    "d"    "m"

'''

class TrieNode(object):
    # We can either use alphabet-len(26) array of boolean
    # but go with dict so we can support more characters, though the requirement contraints don't ask us to do so.
    def __init__(self, ch, val=None, childs=None):
        self.ch = ch
        self.val = None
        self.childs = dict() if childs is None else childs
    
    def add_child(self, ch):
        self.childs[ch] = TrieNode(ch)
        
    def set_val(self, val):
        self.val = val
        
        
class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.childs:
                cur.add_child(c)
            cur = cur.childs[c]
        cur.val = word

    def search(self, word: str) -> bool:
        # check if word exists
        cur = self.root
        for c in word:
            if c not in cur.childs:
                return False
            cur = cur.childs[c]
        if cur.val == word:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.childs:
                return False
            cur = cur.childs[c]
        return True


if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
