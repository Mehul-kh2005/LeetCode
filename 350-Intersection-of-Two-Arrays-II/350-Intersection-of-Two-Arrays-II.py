class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        for num in nums1:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        intersection=[]
        for num in nums2:
            if num in dict1 and dict1[num]>0:
                intersection.append(num)
                dict1[num]-=1
        return intersection