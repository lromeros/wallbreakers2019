from functools import lru_cache

class Solution:
    
    @lru_cache(maxsize=None)
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        if word2[0] == word1[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            insert = 1 + self.minDistance(word2[0] + word1, word2)
            delete = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word2[0] + word1[1:], word2)
            return min(insert, delete, replace)
