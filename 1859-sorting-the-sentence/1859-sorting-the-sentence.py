class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        for w in s.split():
            d[int(w[-1])] = w[:-1]
        
        wl = []
        l = list(d.keys())
        l.sort()
        for i in l:
            wl.append(d[i])

        return " ".join(wl)