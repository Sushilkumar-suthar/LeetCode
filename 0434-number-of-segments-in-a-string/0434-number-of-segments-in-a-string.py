class Solution:
    def countSegments(self, s: str) -> int:
        l = []
        wordCount = 0
        word = ""
        for c in s:
            if c == " " and wordCount > 0:
                l.append(word)
                wordCount = 0
                word = ""
            else:
                
                if c != " ":
                    wordCount += 1
                    word += c

        if wordCount > 0:
            l.append(word)
        return len(l)