class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans=["0"]*len(nums)
        for i in range(len(nums)):
            curr=nums[i][i]
            if curr=="0":
                ans[i]="1"

        return "".join(ans)