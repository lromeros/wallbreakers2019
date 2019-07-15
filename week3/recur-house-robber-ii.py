class Solution:
    def rob_recur(self, nums: List[int], max_at: List[int], index: int):        
        if max_at[index] == -1:
            if len(nums) - index <= 2:
                max_at[index] = max(nums[index:], default=0)
            else:
                self.rob_recur(nums, max_at, index + 2)
                self.rob_recur(nums, max_at, index + 1)
                max_at[index] = max(nums[index] + max_at[index + 2], max_at[index + 1])

    
    def linear_rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)
        else:
            max_at = [-1] * len(nums)
            self.rob_recur(nums, max_at, 0)
            return max_at[0]
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.linear_rob(nums[0:len(nums)-1]), self.linear_rob(nums[1:len(nums)]))
