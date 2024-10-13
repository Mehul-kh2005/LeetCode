class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq=[]
        max_val=float('-inf')
        range_start=0
        range_end=float('inf')

        for i in range(len(nums)):
            heapq.heappush(pq,(nums[i][0],i,0))
            max_val=max(max_val,nums[i][0])

        while len(pq)==len(nums):
            min_val,row,col=heapq.heappop(pq)

            if max_val-min_val<range_end-range_start:
                range_start=min_val
                range_end=max_val

            if col+1<len(nums[row]):
                next_val=nums[row][col+1]
                heapq.heappush(pq,(next_val,row,col+1))
                max_val=max(max_val,next_val)

        return [range_start,range_end]