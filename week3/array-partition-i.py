class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        pair_sum = 0
        
        while i < len(nums):
            pair_sum += nums[i]
            i += 2
        
        return pair_sum
