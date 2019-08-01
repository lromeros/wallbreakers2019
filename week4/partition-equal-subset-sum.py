from functools import lru_cache

class Solution:
    nums = []
    target = 0
    
    @lru_cache(maxsize=None)
    def can_partition(self, a_sum: int, b_sum: int, start: int) -> bool:
        if a_sum == self.target == b_sum:
            return True
        elif b_sum > 0:
            for i in range(start, len(self.nums)):
                num = self.nums[i]

                if a_sum + num <= b_sum - num and self.can_partition(a_sum + num, b_sum - num, i + 1):
                    return True

        return False


    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        total = sum(self.nums)
        
        if total % 2 == 0:
            self.target = total / 2
            return self.can_partition(0, total, 0)

        return False