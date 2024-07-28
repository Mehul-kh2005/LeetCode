class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        total_cost=0

        min_cost=[[float("inf")]*26 for _ in range(26)]

        for orig,chg,cst in zip(original,changed,cost):
            start_char=ord(orig)-ord("a")
            end_char=ord(chg)-ord("a")

            min_cost[start_char][end_char]=min(min_cost[start_char][end_char],cst)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j]=min(min_cost[i][j],min_cost[i][k]+min_cost[k][j])
        
        for src,tgt in zip(source,target):
            if src==tgt:
                continue
            source_char=ord(src)-ord("a")
            target_char=ord(tgt)-ord("a")

            if min_cost[source_char][target_char]==float("inf"):
                return -1

            total_cost+=min_cost[source_char][target_char]

        return total_cost