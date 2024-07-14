class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
                
        n=len(horizontalCut)
        m=len(verticalCut)
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        min_cost=0
        hPieces=1
        vPieces=1
        hIndex=0
        vIndex=0
        
        while hIndex<n or vIndex<m:
            if (hIndex<n) and (vIndex>=m or horizontalCut[hIndex]>=verticalCut[vIndex]):
                min_cost+=horizontalCut[hIndex]*vPieces
                hPieces+=1
                hIndex+=1
            else:
                min_cost+=verticalCut[vIndex]*hPieces
                vPieces+=1
                vIndex+=1
        
        return min_cost