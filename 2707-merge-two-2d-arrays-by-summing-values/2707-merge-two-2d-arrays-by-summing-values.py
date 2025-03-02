class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result=[]
        index1=index2=0

        while index1<len(nums1) and index2<len(nums2):
            if nums1[index1][0]==nums2[index2][0]:
                result.append([nums1[index1][0],nums1[index1][1]+nums2[index2][1]])
                index1+=1
                index2+=1
            elif nums1[index1][0]<nums2[index2][0]:
                result.append([nums1[index1][0],nums1[index1][1]])
                index1+=1
            else:
                result.append([nums2[index2][0],nums2[index2][1]])
                index2+=1

        while index1<len(nums1):
            result.append([nums1[index1][0],nums1[index1][1]])
            index1+=1

        while index2<len(nums2):
            result.append([nums2[index2][0],nums2[index2][1]])
            index2+=1

        return result