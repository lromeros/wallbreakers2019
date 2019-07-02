class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        shorter = nums1
        longer = nums2
        if len(nums1) > len(nums2):
            shorter, longer = longer, shorter
        shorter_dict = {num:0 for num in shorter}
        for n in longer:
            if shorter_dict.get(n) is not None:
                answer.append(n)
        return list(set(answer))
