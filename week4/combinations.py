import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = itertools.combinations(range(1,n+1), k)
        
        return combinations
