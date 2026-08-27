class Solution:
    def hasGroupsSizeX(self, deck):
        count = {}
        for card in deck:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1
        g = 0
        for freq in count.values():
            a = g
            b = freq

            while b != 0:
                a, b = b, a % b

            g = a

        return g > 1