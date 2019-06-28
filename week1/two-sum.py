class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl_ind_dict = {}
        
        for i in range(len(nums)):
            n = nums[i]
            if compl_ind_dict.get(target-n) is not None:
                return [compl_ind_dict.get(target-n), i]
            else:
                compl_ind_dict[n] = i
