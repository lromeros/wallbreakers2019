class Solution:
    def linear_rob(self, nums: List[int]) -> int:
        sums = []
        
        for i in range(len(nums)):
            sums.append([0, False])
            
        if len(nums) == 0:
            return 0
        elif len(nums) > 1:
            sums[1][0] = nums[1] if nums[0] < nums[1] else nums[0]
            sums[1][1] = nums[0] < nums[1]
            
        sums[0] = [nums[0], True]
        
        for i in range(2, len(nums)):
            if sums[i-1][1] == True:
                sums[i][1] = nums[i] + sums[i-2][0] > sums[i-1][0]
                sums[i][0] = nums[i] + sums[i-2][0] if sums[i][1] else sums[i-1][0]
            else:
                sums[i][0] = sums[i-1][0] + nums[i]
                sums[i][1] = True
        
        return sums[len(nums) - 1][0]
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.linear_rob(nums[0:len(nums)-1]), self.linear_rob(nums[1:len(nums)]))
