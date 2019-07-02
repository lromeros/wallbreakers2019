class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {j:0 for j in J}
        counter = 0
        for s in S:
            if jewels.get(s) is not None:
                counter += 1
        return counter
