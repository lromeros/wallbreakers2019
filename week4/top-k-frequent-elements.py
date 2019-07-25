from collections import Counter
import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > 0:
            counter = [(count, number) for number, count in Counter(nums).items()]
            heapq.heapify(counter)
            return [item[1] for item in heapq.nlargest(k, counter)]

