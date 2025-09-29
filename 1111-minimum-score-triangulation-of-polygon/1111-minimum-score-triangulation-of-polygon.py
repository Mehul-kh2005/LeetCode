import math

class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        
        # dp[i][j] will store the minimum score to triangulate the polygon
        # formed by vertices values[i], values[i+1], ..., values[j]
        dp = [[0] * n for _ in range(n)]

        # len_poly represents the number of vertices in the current sub-polygon
        # It ranges from 3 to n (inclusive)
        for len_poly in range(3, n + 1):
            # i is the starting index of the sub-polygon
            for i in range(n - len_poly + 1):
                j = i + len_poly - 1  # j is the ending index of the sub-polygon
                
                # Initialize dp[i][j] with a very large value
                dp[i][j] = float('inf')
                
                # k is the third vertex of the triangle (values[i], values[k], values[j])
                # It must be strictly between i and j
                for k in range(i + 1, j):
                    score_triangle = values[i] * values[k] * values[j]
                    
                    # The total score for this choice of k is:
                    # score_triangle + min_score_for_sub_polygon(i, k) + min_score_for_sub_polygon(k, j)
                    current_score = score_triangle + dp[i][k] + dp[k][j]
                    
                    # Update dp[i][j] with the minimum score found so far
                    dp[i][j] = min(dp[i][j], current_score)
        
        # The result is the minimum score for the entire polygon (from vertex 0 to n-1)
        return dp[0][n - 1]