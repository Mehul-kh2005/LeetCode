class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers=set(loser for _,loser in edges)
        potential_champions=set(range(n))-losers

        return next(iter(potential_champions)) if len(potential_champions)==1 else -1