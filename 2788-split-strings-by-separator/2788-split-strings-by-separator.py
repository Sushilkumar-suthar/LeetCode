class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        if len(words)==0:return []
        l = []
        for i in words:
            l+=[j for j in i.split(separator) if j.strip()!=""]
        return l
