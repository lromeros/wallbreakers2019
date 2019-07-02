from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = Counter(p)
        freq_s = Counter(s[0:len(p)])
        indices = []
        
        for i in range(len(p), len(s) + 1):
            if freq_p == freq_s:
                indices.append(i - len(p))
            if i >= len(s):
                break
            freq_s[s[i]] += 1
            freq_s[s[i-len(p)]] -= 1
            if freq_s[s[i-len(p)]] == 0:
                freq_s.pop(s[i-len(p)])
                
        return indices
      
