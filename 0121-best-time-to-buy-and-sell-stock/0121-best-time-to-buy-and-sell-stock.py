class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=prices[0]
        profit=0

        for price in prices[1:]:
            if buy_price>price:
                buy_price=price

            profit=max(profit,price-buy_price)

        return profit