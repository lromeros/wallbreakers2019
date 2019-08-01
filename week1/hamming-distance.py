class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming = 0
        
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                hamming += 1
            x = math.floor(x / 2)
            y = math.floor(y / 2)
        
        return hamming
