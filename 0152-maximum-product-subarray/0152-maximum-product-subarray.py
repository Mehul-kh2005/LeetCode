class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=min_product=global_product=nums[0]

        for i in range(1,len(nums)):
            if nums[i]<0:
                max_product,min_product=min_product,max_product

            max_product=max(nums[i],max_product*nums[i])
            min_product=min(nums[i],min_product*nums[i])

            global_product=max(global_product,max_product)

        return global_product