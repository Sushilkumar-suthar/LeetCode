class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[int(i==0) for i in row[::-1]]
            for row in image]