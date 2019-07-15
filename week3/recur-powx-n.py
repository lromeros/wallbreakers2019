class Solution:
    def myCachedPow(self, x: float, n: int, cache: dict) -> float:
        if cache.get(n) is not None:
            return cache.get(n)
        elif cache.get(n * -1) is not None:
            return 1 / cache.get(n * -1)
        elif n % 2 == 0:
            half = n/2
            if cache.get(half) is None:
                cache[half] = self.myCachedPow(x, half, cache)
            return cache.get(half) * cache.get(half)
        else:
            cache[n] = x * self.myCachedPow(x, n-1, cache)
            return cache.get(n)
        
    def myPow(self, x: float, n: int) -> float:
        return self.myCachedPow(x, n, {0:1, 1:x})
