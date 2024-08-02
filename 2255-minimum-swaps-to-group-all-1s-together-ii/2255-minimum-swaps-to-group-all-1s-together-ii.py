class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        group_0=self.minSwapsHelper(nums,0)
        group_1=self.minSwapsHelper(nums,1)

        return min(group_0,group_1)

    def minSwapsHelper(self,nums,val):
        length=len(nums)
        total_val_count=nums.count(val)

        if total_val_count==0 or total_val_count==length:
            return 0

        start=0
        end=0
        current_val_in_window=0
        max_val_in_window=0

        while end<total_val_count:
            if nums[end]==val:
                current_val_in_window+=1
            end+=1

        max_val_in_window=max(max_val_in_window,current_val_in_window)

        while end<length:
            if nums[start]==val:
                current_val_in_window-=1
            start+=1

            if nums[end]==val:
                current_val_in_window+=1
            end+=1

            max_val_in_window=max(max_val_in_window,current_val_in_window)

        return total_val_count-max_val_in_window