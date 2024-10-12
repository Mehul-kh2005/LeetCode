import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h=[]

        for start,end in intervals:
            if h and start>h[0]:
                heapq.heappop(h)

            heapq.heappush(h,end)

        return len(h)