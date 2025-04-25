class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        target=n//3

        el1=el2=float('inf')
        count1=count2=0

        for num in nums:
            if count1==0 and num!=el2:
                el1=num
                count1+=1

            elif count2==0 and num!=el1:
                el2=num
                count2+=1

            elif num==el1:
                count1+=1

            elif num==el2:
                count2+=1

            else:
                count1-=1
                count2-=1

        count1=count2=0
        result=[]

        for num in nums:
            if num==el1:
                count1+=1
            
            if num==el2:
                count2+=1
        
        if count1>target:
            result.append(el1)

        if count2>target:
            result.append(el2)

        return result            