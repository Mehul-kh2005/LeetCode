class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        decrement,sum=0,0
        for i in range (k):
            element=happiness.pop()
            if element-decrement>=0:
                sum+=element-decrement
                decrement+=1
        return sum