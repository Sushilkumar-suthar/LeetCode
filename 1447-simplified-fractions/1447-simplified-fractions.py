class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        d = []
        for i in range(1,n):
            for j in range(i+1,n+1):
                if i/j not in d:
                    d.append(i/j)
                    result.append(f"{i}/{j}")
        return result