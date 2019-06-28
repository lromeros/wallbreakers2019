class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            freq_dict = {}
            for i in range(len(s)):
                freq_dict[s[i]] = freq_dict.get(s[i], 0) + 1
                freq_dict[t[i]] = freq_dict.get(t[i], 0) - 1
            for e in freq_dict.values():
                if e != 0:
                    return False
            return True
        else:
            return False
