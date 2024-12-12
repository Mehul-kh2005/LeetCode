class Solution:
    def pickGifts(self, gifts, k):
        # Create a max-heap from the 'gifts' array (negating values to simulate max-heap)
        gifts_heap = [-gift for gift in gifts]
        heapq.heapify(gifts_heap)

        # Perform the operation 'k' times
        for _ in range(k):
            # Get the maximum element from the heap (top element)
            max_element = -heapq.heappop(gifts_heap)

            # Insert the floor of the square root of the maximum element back into the heap
            heapq.heappush(gifts_heap, -math.floor(math.sqrt(max_element)))

        # Accumulate the sum of the elements in the heap
        number_of_remaining_gifts = 0
        while gifts_heap:
            number_of_remaining_gifts -= heapq.heappop(gifts_heap)

        return number_of_remaining_gifts