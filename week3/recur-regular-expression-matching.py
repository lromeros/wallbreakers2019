from functools import lru_cache

class Solution:
    def regexEquals(self, a: str, b: str) -> bool:
        if b == '.':
            return True
        else:
            return a == b
        
        
    @lru_cache(maxsize=None)
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) > 1 and len(s) > 0:
            if p[1] == '*':
                ignore = self.isMatch(s, p[2:])  # starred element appears 0 times
                once = self.regexEquals(s[0], p[0]) and self.isMatch(s[1:], p[2:])  # starred element appears 1 times
                mult = self.regexEquals(s[0], p[0]) and self.isMatch(s[1:], p)  # starred element appears 1< times
                return ignore or once or mult
            elif self.regexEquals(s[0], p[0]):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        elif len(s) > len(p): # len(s) >= 1 and len(p) == 0 
            return False
        elif len(p) > 0 and len(s) == 0:
            if len(p) >= 2 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False
        elif len(p) == len(s):
            return self.regexEquals(s, p)
