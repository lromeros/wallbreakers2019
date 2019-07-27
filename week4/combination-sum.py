class Solution:
    def valid_combination_sum(self, combinations: List[List[int]], chosen: List[int], candidates: List[int], target: int) -> bool:
        _sum = sum(chosen)

        if _sum < target:
            for num in candidates:
                chosen.append(num)
                chosen.sort()
                if self.valid_combination_sum(combinations, chosen, candidates, target):
                    combinations.append(copy.copy(chosen))

                chosen.remove(num)

                    
        return _sum == target and chosen not in combinations
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        if target == 0:
            return [[]]
        
        self.valid_combination_sum(combinations, [], candidates, target)
                
        return combinations
