class Solution:
    def create_min_max_profit_list(self, size: int, first_val: int) -> List[List[int]]:
        min_max_profit = [] 
        min_max_profit.append([first_val, first_val, 0])
        
        for i in range(1, size):
            min_max_profit.append([0,0,0])
        
        return min_max_profit
    
    
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        # min so far, max so far, best profit so far
        min_max_profit = [[prices[0], prices[0], 0]]
        
        for i in range(1, len(prices)):
            new_min =  min_max_profit[i - 1][0]
            new_max =  min_max_profit[i - 1][1]
                
            if prices[i] < min_max_profit[i - 1][0]:
                new_min =  prices[i]
                new_max =  prices[i]
            elif prices[i] > min_max_profit[i - 1][1]:
                new_max =  prices[i]
                
            new_profit = max(new_max - new_min, min_max_profit[i-1][2])
            min_max_profit.append([new_min, new_max, new_profit])
            
        return min_max_profit[len(prices) - 1][2]
        
