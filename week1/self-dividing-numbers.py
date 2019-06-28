class Solution:
    def is_self_dividing(self, x):
        self_dividing = True
        ints = [int(c) for c in str(x)]
        for i in ints:
            if i == 0 or x % i != 0:
                self_dividing = False
                break
        return self_dividing
    
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for x in range(left, right + 1):
            if x % 10 == 0:
                pass
            elif x < 10 or self.is_self_dividing(x):
                answer.append(x)
        return answer
