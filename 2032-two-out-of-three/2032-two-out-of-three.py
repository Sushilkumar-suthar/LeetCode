class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = []
        l1, l2, l3 = len(nums1), len(nums2), len(nums3)
        cl = list(set(nums1+nums2+nums3))
        for i in cl:
            c=0
            if i in nums1:c+=1
            if i in nums2:c+=1
            if i in nums3:c+=1
            if c>=2:result.append(i)
        return result