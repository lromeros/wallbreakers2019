from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        answer = [0, 0]
        
        for i in range(1, len(nums) + 1):
            if answer[0] != 0 and answer[1] != 0:
                break
            if counter.get(i) is not None:
                if counter.get(i) > 1:
                    answer[0] = i
            else:
                answer[1] = i
                
        return answer
