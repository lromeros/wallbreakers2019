class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length_left = len(nums)
        k = k % length_left
        last_index = 0
        pos = 0

        while k != 0 and length_left > 0:
            for pos in range(k):
                swap_val = len(nums) - k + pos
                nums[last_index + pos], nums[swap_val] = nums[swap_val], nums[last_index + pos]
                 
            length_left -= k
            last_index += k
            k = k % length_left
