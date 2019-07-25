class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')':'(', '}':'{', ']':'['}
        parens = []
        
        for paren in s:
            if paren in close_open.values():
                parens.append(paren)
            else:
                if len(parens) < 1 or close_open.get(paren) != parens.pop():
                    return False
                
        return len(parens) == 0
                
