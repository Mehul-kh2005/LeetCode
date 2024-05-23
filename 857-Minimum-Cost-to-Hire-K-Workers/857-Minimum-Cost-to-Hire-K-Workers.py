class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
        min_cost = float('inf')
        total_quality = 0
        heap = []

        for ratio, qual in workers:
            heapq.heappush(heap, -qual)
            total_quality += qual
            
            if len(heap) > k:
                total_quality += heapq.heappop(heap)

            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost