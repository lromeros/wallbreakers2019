class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        i = 0
        
        for c in t:
            if i < s_len:
                if c == s[i]:
                    i += 1
            else:
                return True
        
        return i == s_len
