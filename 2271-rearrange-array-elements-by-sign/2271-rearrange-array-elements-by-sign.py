class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        pos_idx,neg_idx=0,1

        for i in range(len(nums)):
            if nums[i]>0:
                result[pos_idx]=nums[i]
                pos_idx+=2

            else:
                result[neg_idx]=nums[i]
                neg_idx+=2

        return result