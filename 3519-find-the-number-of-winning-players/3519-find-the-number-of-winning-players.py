class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        result = 0
        players = defaultdict(lambda: defaultdict(int))
        
        for p, c in pick:
            players[p][c] += 1
            
        for p in range(n):
            if any(count > p for count in players[p].values()):
                result += 1
                
        return result