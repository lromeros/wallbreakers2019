import bisect

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(list(p))        
        slice_s = sorted(s[0:len(p)])
        indices = []
        
        for i in range(len(p), len(s) + 1):
            if p == slice_s:
                indices.append(i - len(p))
            if i >= len(s):
                break
            slice_s.remove(s[i - len(p)])
            bisect.insort_left(slice_s, s[i])
                
        return indices
      
