import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = itertools.permutations(nums, len(nums))
        
        return permutations
