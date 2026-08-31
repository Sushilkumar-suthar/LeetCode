class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        if len(words)==0:return []
        l = []
        for i in words:
            l.extend([j for j in i.split(separator) if len(j.strip())!=0])
        return l
