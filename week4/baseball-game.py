class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rounds = []
        
        for op in ops:
            if op == '+':
                new_round = rounds[-1] + rounds[-2]
                rounds.append(new_round)
            elif op == 'D':
                new_round = 2 * rounds[-1] if len(rounds) > 0 else 0
                rounds.append(new_round)
            elif op == 'C':
                rounds.pop()
            else:
                rounds.append(int(op))
                
        return sum(rounds)
