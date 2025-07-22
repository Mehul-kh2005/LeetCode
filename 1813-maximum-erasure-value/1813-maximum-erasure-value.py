class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result,left,curr_sum=0,0,0
        seen=set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum-=nums[left]
                left+=1

            curr_sum+=nums[right]
            seen.add(nums[right])
            result=max(result,curr_sum)

        return result