class Solution:
    num_buckets = 2
    target = 0
    
    def can_partition(self, a_sum: int, b_sum: int, nums: List[int]) -> bool:
        print(f"a_sum:{a_sum},b_sum:{b_sum}")
        if a_sum == self.target == b_sum:
            return True
        elif b_sum > 0:
            for i in range(len(nums)):
                num = nums[i]
                if a_sum + num <= b_sum - num and self.can_partition(a_sum + num, b_sum - num, nums[i+1:]):
                    return True
        else:
            return False
            
        
        
    def canPartition(self, nums: List[int]) -> bool:
        print("==========================================")
        total = sum(nums)
        if total % self.num_buckets == 0:
            self.target = total / self.num_buckets
            return self.can_partition(0, total, nums)
        else:
            return False
