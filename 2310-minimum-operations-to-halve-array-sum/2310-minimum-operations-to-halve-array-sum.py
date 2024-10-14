import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = sum(nums) 
        half_sum = total_sum / 2 
        count = 0  
        current_sum = total_sum  
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        while current_sum > half_sum:
            max_ele = heapq.heappop(nums)  
            current_sum += max_ele / 2 
            heapq.heappush(nums, max_ele / 2)  
            count += 1  
        return count