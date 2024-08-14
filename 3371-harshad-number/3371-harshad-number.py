class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        num=x
        while x!=0:
            sum+=x%10
            x=x//10
        if num%sum==0:
            return sum
        return -1