class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_locs = {}
        t_locs = {}
        
        for i in range(len(s)):
            if s_locs.get(s[i]) is not None:
                s_locs.get(s[i]).append(i)
            else:
                s_locs[s[i]] = [i]
            
            if t_locs.get(t[i]) is not None:
                t_locs.get(t[i]).append(i)
            else:
                t_locs[t[i]] = [i]
                
            if s_locs.get(s[i]) != t_locs.get(t[i]):
                return False
            
        return True
