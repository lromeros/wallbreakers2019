class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n % 2 != 0:
                return n == 1
            else:
                n = n/2
                
        return False
