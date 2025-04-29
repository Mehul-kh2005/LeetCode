class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        max_ele=max(nums)
        start,count_in_window=0,0
        result=0

        for i in range(n):
            if nums[i]==max_ele:
                count_in_window+=1

            end=i
            while start<=end and count_in_window>=k:
                if nums[start]==max_ele:
                    count_in_window-=1

                start+=1

            result+=start

        return result