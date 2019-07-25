class Solution:
    def scoreOfParenthesesRecur(self, S: str, index: int):
        open_close = {'(':')', '{':'}', '[':']'}
        is_open = False
        i = -1
        _sum = 0
        
        while i < len(S) - 1:
            i += 1
            paren = S[i]

            if paren in open_close.keys():
                if not is_open:
                    is_open = True
                else:
                    new_sum, i_delta = self.scoreOfParenthesesRecur(S[i:], 0)
                    _sum += 2 * new_sum
                    i += i_delta
                    is_open = False
                    
            elif is_open:
                _sum += 1
                is_open = False
            else:
                break
            
        return _sum, i

    
    def scoreOfParentheses(self, S: str) -> int:
        return self.scoreOfParenthesesRecur(S, 0)[0]

