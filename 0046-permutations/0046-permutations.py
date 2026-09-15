class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        
        for n in nums:
            new_res = []
            for p in res:
                for i in range(len(p) + 1):
                    new_res.append(p[:i] + [n] + p[i:])
            res = new_res
            
        return res