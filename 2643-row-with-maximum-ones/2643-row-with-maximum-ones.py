class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = 0
        maxi = 0

        for i in range(len(mat)):
            count = sum(mat[i])

            if count > maxi:
                maxi = count
                ans = i

        return [ans, maxi]