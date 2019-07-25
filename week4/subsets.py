import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        for i in range(len(nums) + 1):
            subsets.extend(itertools.combinations(nums, i))
            
        return subsets
