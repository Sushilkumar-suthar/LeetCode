class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        while bool(nums1) and bool(nums2):
            if nums1[0]<nums2[0]:
                result.append(nums1[0])
                nums1.pop(0)
            else:
                result.append(nums2[0])
                nums2.pop(0)
        result+= list(nums1+nums2)
        l = len(result)
        return result[int((l+1)/2)-1] if l%2!=0 else (result[int(l/2)-1]+result[int(l/2)])/2