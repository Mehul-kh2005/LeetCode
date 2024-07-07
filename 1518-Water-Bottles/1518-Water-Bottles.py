class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = 0

        while numBottles >= numExchange:
            K = numBottles // numExchange

            consumed_bottles += numExchange * K
            numBottles -= numExchange * K

            numBottles += K

        return consumed_bottles + numBottles