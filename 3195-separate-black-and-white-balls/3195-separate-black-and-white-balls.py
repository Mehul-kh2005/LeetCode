class Solution:
    def minimumSteps(self, s: str) -> int:
        total_swaps=0
        black_ball_count=0
        
        for char in s:
            if char=='0':
                total_swaps+=black_ball_count
            else:
                black_ball_count+=1

        return total_swaps