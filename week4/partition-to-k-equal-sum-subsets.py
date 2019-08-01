class Solution:
    def can_partition(self, k: int, start_i: int, subtotal: int, target: int, nums: List[int], nums_used: List[int]) -> bool:
        if k == 1:
            return True
        if subtotal == target:
            return self.can_partition(k-1, 0, 0, target, nums, nums_used)

        for i in range(start_i, len(nums)):
            if not nums_used[i]:
                nums_used[i] = True
                sum_within_range = subtotal + nums[i] <= target
                if sum_within_range and self.can_partition(k, i + 1, subtotal + nums[i], target, nums, nums_used):
                    return True
                nums_used[i] = False
                
        return False
        
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        
        if total % k == 0:
            target = total / k
            nums_used = [False for _ in range(len(nums))]
            
            return self.can_partition(k, 0, 0, target, nums, nums_used)

        return False

