class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n != 1:
            digs = str(n)
            n = 0
            for d in digs:
                n += int(d) ** 2
            if seen.get(n) is not None:
                return False
            else:
                seen[n] = 0
        return True
                
