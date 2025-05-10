class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1=sum2=0
        zero1=zero2=0

        for i in nums1:
            sum1+=i
            if i==0:
                sum1+=1
                zero1+=1

        for i in nums2:
            sum2+=i
            if i==0:
                sum2+=1
                zero2+=1

        if (sum1<sum2 and zero1==0) or (sum2<sum1 and zero2==0):
            return -1

        return max(sum1,sum2)