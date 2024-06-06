class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        hand = sorted(hand)
        for num in hand:
            if freq[num]:
                for i in range(num,num + groupSize):
                    freq[i] -= 1
                    if freq[i] < 0:
                        return False
        return True