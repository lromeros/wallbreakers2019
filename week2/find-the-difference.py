from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s = Counter(s)
        freq_t = Counter(t)
        
        for c in t:
            if freq_s.get(c) is None or freq_s.get(c) != freq_t.get(c):
                return c
        
