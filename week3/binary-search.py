class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = math.floor(len(nums) / 2)
        upper_bound = len(nums)
        lower_bound = 0
        num_seen = 1
        
        while nums[index] != target and num_seen < len(nums):
            if nums[index] < target:
                lower_bound = index
                index += math.floor((upper_bound - lower_bound) / 2)
            else:
                upper_bound = index
                index = math.floor(upper_bound / 2)
            num_seen += 1
                
        return index if nums[index] == target else -1
