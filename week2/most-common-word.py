from collections import Counter

class Solution:
    def clean_paragraph(self, paragraph, banned):
        clean = []
        breaks = ["!", "?", "'", ",", ";", ".", " "]
        word = ''
        for c in paragraph:
            if c not in breaks:
                word += c.lower()
            else:
                if word not in banned:
                    if len(word) > 0:
                        clean.append(word)
                word = ''
        if len(word) > 0 and word not in banned:
            clean.append(word)
            
        return clean
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = self.clean_paragraph(paragraph, banned)
        return Counter(paragraph).most_common(1)[0][0]

