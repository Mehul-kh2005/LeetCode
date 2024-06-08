class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map={0:-1}
        sum=0

        for i in range(len(nums)):
            sum+=nums[i]
            remainder=sum%k

            if remainder in map:
                if i-map[remainder]>1:
                    return True
            else:
                map[remainder]=i

        return False