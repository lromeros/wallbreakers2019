class Solution:
    def insert_at_all_i(self, result: str) -> List[str]:
        results = []
        results.append('(' + result +')')
        
        for i in range(len(result) + 1):
            results.append(result[:i] + '()' + result[i:])
            
        return results
        
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        
        if n == 0:
            return ['']
        else:
            recurse = self.generateParenthesis(n-1)
            
            for result in recurse:
                combs.extend(self.insert_at_all_i(result))

        return set(combs)
