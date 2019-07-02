class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        # dictionary of sorted even letters, where value is sorted odd letters
        groups = {}
        for a in A:
            evens = []
            odds = []
            
            for i in range(len(a)):
                if i % 2 == 0:
                    evens.append(a[i])
                else:
                    odds.append(a[i])
            evens.sort()
            evens = ''.join(evens)
            odds = odds.sort()
            
            if groups.get(evens) is None:
                groups[evens] = [odds]
            else:
                if not odds in groups.get(evens):
                    groups[evens].append(odds)

        return len(groups.keys())
