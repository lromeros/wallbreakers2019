class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_count = len([c for c in word if c.isupper()])
        if cap_count == 0 or cap_count == len(word):
            return True
        elif cap_count == 1:
            return word[0].isupper()
        else:
            return False
            
