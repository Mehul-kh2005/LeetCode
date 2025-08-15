class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splitArrayPossible(max_sum):
            subarray=1
            curr_sum=0

            for i in range(len(nums)):
                if curr_sum+nums[i]<=max_sum:
                    curr_sum+=nums[i]

                else:
                    subarray+=1
                    curr_sum=nums[i]

                if subarray>k:
                    return False

            return True

        low=max(nums)
        high=sum(nums)

        while low<=high:
            mid=(low+high)//2

            if splitArrayPossible(mid):
                high=mid-1

            else:
                low=mid+1

        return low