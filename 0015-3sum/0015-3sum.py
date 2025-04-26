class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        nums.sort()
        
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            j=i+1
            k=n-1

            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1

                    while j<k and nums[k]==nums[k+1]:
                        k-=1

                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1

                else:
                    j+=1

        return result