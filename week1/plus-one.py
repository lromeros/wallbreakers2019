class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_ind = len(digits) - 1
        digits[last_ind] += 1
        
        if digits[last_ind] > 9:
            if len(digits) == 1:
                return [1, 0]
            else:
                digits = self.plusOne(digits[0:last_ind])
                digits.append(0)
                
        return digits
