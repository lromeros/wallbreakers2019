class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern = [c for c in pattern]
        string = str.split(' ')
        if len(pattern) == len(string):
            return len(set(pattern)) == len(set(string)) == len(set(zip(pattern, string)))
        else:
            return False
