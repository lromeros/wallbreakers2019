class Trie:

    def __init__(self, char='', terminal=False):
        """
        Initialize your data structure here.
        """
        
        self.character = char
        self.children = {}
        self.terminal = terminal

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) > 0:
            char = word[0]
            if self.children.get(char) is None:
                self.children[char] = Trie(char)
        if len(word) == 1:
            self.children[char].terminal = True
        elif len(word) > 1:
            self.children[char].insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:
            return True
        
        char = word[0]
        if self.children.get(char) is not None:
            if len(word) == 1:
                return self.children.get(char).terminal
            else:
                return self.children.get(char).search(word[1:]) 
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:
            return True
        
        char = prefix[0]
                
        if self.children.get(char) is not None and len(prefix) == 1:
            return True
        elif self.children.get(char) is not None:
            return self.children.get(char).startsWith(prefix[1:]) 
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
