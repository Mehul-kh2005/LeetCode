class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longest_streak=0
        num_set=set(nums)

        for start_number in nums:
            curr_number=start_number
            curr_streak=0

            while curr_number in num_set:
                curr_streak+=1

                if curr_number*curr_number>10**5:
                    break
                
                curr_number*=curr_number

            longest_streak=max(longest_streak,curr_streak)

        return longest_streak if longest_streak>1 else -1