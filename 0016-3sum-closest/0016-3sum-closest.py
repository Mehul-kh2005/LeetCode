class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        ans=float('inf')

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            j=i+1
            k=n-1

            while j<k:
                total=nums[i]+nums[j]+nums[k]
                
                if abs(target-total)<abs(target-ans):
                    ans=total

                if total<target:
                    j+=1
                    
                elif total>target:
                    k-=1
                                        
                else:
                    # If total == target, this is the closest possible
                    return total

        return ans