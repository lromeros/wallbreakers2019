class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        i = 0
        
        while num > 1:
            if num % 2 == 0:
                complement += 2**i
            num = num >> 1
            i += 1
            
        return complement
