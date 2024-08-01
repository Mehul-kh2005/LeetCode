class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()

        if len(stockPrices)<2:
            return 0
        if len(stockPrices)==2:
            return 1

        lines=0
        prev_slope=None

        for i in range(1,len(stockPrices)):
            x1,y1=stockPrices[i-1]
            x2,y2=stockPrices[i]

            dx=x2-x1
            dy=y2-y1

            gcd_val=gcd(dy,dx)
            slope=(dy//gcd_val,dx//gcd_val)

            if slope!=prev_slope:
                lines+=1
                prev_slope=slope

        return lines