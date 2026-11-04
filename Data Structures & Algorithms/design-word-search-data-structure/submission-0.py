class TrieNode:
    def __init__(self):
        self.children = {}      # maps a letter to the next TrieNode, e.g. {"a": <node>}
        self.is_end = False     # True if a word ends at this node

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  # empty root node; every word starts from here

    def addWord(self, word: str) -> None:
        node = self.root                       # start at the root
        for ch in word:                        # go through the word one letter at a time
            if ch not in node.children:        # no path for this letter yet?
                node.children[ch] = TrieNode() # create a new node for it
            node = node.children[ch]           # move down into that node
        node.is_end = True                     # mark that a full word ends here

    def search(self, word: str) -> bool:
        def dfs(i, node):
            # i = index of the letter of word we need to match now
            # node = the trie node we are currently standing on

            if i == len(word):                 # we've matched every letter
                return node.is_end             # only a real word if one ends at this node

            ch = word[i]                       # the letter we need to match now

            if ch == ".":                      # wildcard: could be any letter
                for child in node.children.values():  # try every possible child
                    if dfs(i + 1, child):      # if any child leads to a match...
                        return True            # ...we're done
                return False                   # none of the children worked
            else:                              # normal letter
                if ch not in node.children:    # no path for this letter
                    return False               # dead end
                return dfs(i + 1, node.children[ch])  # follow the one matching child

        return dfs(0, self.root)               # start at letter 0, at the root