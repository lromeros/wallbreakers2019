class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        sisters = set(candies)
        
        if len(sisters) > (len(candies) / 2):
            return math.floor(len(candies) / 2)
        else:
            return len(sisters)
