class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        x=nums[0]
        count=0
        xCount=0
        length=len(nums)

        for num in nums:
            if num==x:
                count+=1
            else:
                count-=1

            if count==0:
                x=num
                count+=1

        for num in nums:
            if num==x:
                xCount+=1

        count=0
        for i in range(length):
            if nums[i]==x:
                count+=1
            
            remCount=xCount-count
            if (count>(i+1)//2) and (remCount>(length-i-1)//2):
                return i

        return -1