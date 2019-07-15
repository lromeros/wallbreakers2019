class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5:0, 10:0, 20:0}
        all_change = True
        
        for b in bills:
            if b == 5:
                cash[5] += 1
            elif b == 10:
                if cash[5] >= 1:
                    cash[5] -= 1
                    cash[10] += 1
                else:
                    all_change = False
                    break
            elif b == 20:
                if cash[10] >= 1 and cash[5] >= 1:
                    cash[10] -= 1
                    cash[5] -= 1
                elif cash[5] >= 3:
                    cash[5] -= 3
                else:
                    all_change = False
                    break
                cash[20] += 1
        
        return all_change
