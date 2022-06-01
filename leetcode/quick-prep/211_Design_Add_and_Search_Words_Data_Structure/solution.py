# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

	WordDictionary() Initializes the object.
	void addWord(word) Adds word to the data structure, it can be matched later.
	bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

	1 <= word.length <= 25
	word in addWord consists of lowercase English letters.
	word in search consist of '.' or lowercase English letters.
	There will be at most 3 dots in word for search queries.
	At most 104 calls will be made to addWord and search.
"""
import pytest


class TrieNode:
    def __init__(self):
        self.children = dict() # a: TrieNode ..
        self.isWord = False


class WordDictionary:
    # Trie as our base data structure for searching with wild cards
    # This is basically a prefix tree
    def __init__(self):
        self.root = TrieNode() # Empty root intialized
    
    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        
    def search(self, word: str) -> bool:
        # "." wildcard supported different from "*" so 
        def dfs(k, root):
            cur = root
            
            for i in range(k, len(word)):
                c = word[i]

                if c == ".":
                    # backtrack through ".ab"
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False    
                else:
                    # regular chars
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            # terminal node must be a word
            return cur.isWord
        return dfs(0, self.root)



@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
     [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]],
     [None,None,None,None,False,True,True,True]),
    (["WordDictionary","addWord","addWord","search","search","search","search","search","search"],
     [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]],
     [[],None,None,True,True,False,True,False,False]),
])
def test(commands, arguments, expecteds):
    obj = WordDictionary(*arguments[0])
    for cmd, arg, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*arg)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
