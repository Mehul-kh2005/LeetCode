class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        result=0
        rotation=0
        for i in range(len(nums)):
            if i>=nums[i]:
                result+=1
        
        for i in range(1,len(nums)):
            count=0
            nums[:]=nums[1:]+nums[:1]
            for idx,value in enumerate(nums):
                if idx>=value:
                    count+=1
            if count>result:
                result=max(result,count)
                rotation=i

        return rotation