class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            num=digits[i]+carry
            digits[i]=num%10
            carry=num//10

        if carry:
            digits.insert(0,carry)

        return digits