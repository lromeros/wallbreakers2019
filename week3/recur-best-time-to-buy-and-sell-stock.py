class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        break_pt = math.ceil(len(prices) / 2)
        left = prices[0:break_pt]
        right = prices[break_pt:len(prices)]
        min_here = min(left)
        max_here = max(right)
        max_sub_profit = max(self.maxProfit(left), self.maxProfit(right))
        return max(max_here - min_here, max_sub_profit)
            
