class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.val = "" # store the word if is_word=True

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
        cur.val = word
  
    def searchWord(self, word):
        """Add wildcard support
        '.' => can traverse all child
        DFS recursion
        - stack iteration on mulitway tree is difficult
        """
        # search for word[i:]
        def dfs(cur, i):
            if i == len(word):
                return cur.is_word

            if word[i] == ".":
                return any(
                    dfs(cur.children[c], i+1)
                    for c in cur.children
                )
            elif word[i] in cur.children:
                return dfs(cur.children[word[i]], i+1)
            return False
        
        return dfs(self.root, 0)
  
    def getAll(self):
        ans = []
  
        def dfs(cur):
            if cur.is_word:
                ans.append(cur.val)
            for c in cur.children.values():
                dfs(c)
        dfs(self.root) 
        return ans


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def add_word(self, word):
        self.trie.addWord(word)

    def search_word(self, word):
        return self.trie.searchWord(word)

    def get_words(self):
        return self.trie.getAll()
