class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Iterate over each book
        for i in range(1, n + 1):
            width = 0
            height = 0
            # Iterate backwards to find all valid placements of books on the current shelf
            for j in range(i, 0, -1):
                width += books[j - 1][0]
                height = max(height, books[j - 1][1])
                if width > shelfWidth:
                    break
                dp[i] = min(dp[i], dp[j - 1] + height)
        
        return dp[n]