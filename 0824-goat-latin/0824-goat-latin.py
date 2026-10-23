class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        result = []
        vowels = "aeiouAEIOU"

        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"

            goat_word += "a" * i
            result.append(goat_word)

        return " ".join(result)