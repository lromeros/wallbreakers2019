class Solution:
    def binaryGap(self, N: int) -> int:
        max_dist = 0
        ones_found = 0
        streak = 1
        
        while N > 0:
            if N % 2 == 1:
                ones_found += 1
                if max_dist < streak:
                    max_dist = streak
                streak = 1
            elif ones_found:
                streak += 1
                
            N = N >> 1
        
        return max_dist if ones_found > 1 else 0
