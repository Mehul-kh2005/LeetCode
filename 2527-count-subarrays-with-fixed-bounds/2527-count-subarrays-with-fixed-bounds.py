class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minIndex=-1
        maxIndex=-1
        badIndex=-1
        count=0

        for i in range(len(nums)):
            if nums[i]==minK:
                minIndex=i

            if nums[i]==maxK:
                maxIndex=i

            if nums[i]<minK or nums[i]>maxK:
                badIndex=i

            if minIndex!=-1 and maxIndex!=-1:
                count+=max(0,min(minIndex,maxIndex)-badIndex)

        return count