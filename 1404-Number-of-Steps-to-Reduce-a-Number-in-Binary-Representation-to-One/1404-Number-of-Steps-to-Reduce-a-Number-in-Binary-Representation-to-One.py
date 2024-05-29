class Solution:
    def numSteps(self, s: str) -> int:
        l = len(s) - 1
        carry = 0
        count = 0
        while (l > 0):
            if int(s[l]) + carry == 0:
                carry = 0
                count += 1
            elif int(s[l]) + carry == 2:
                carry = 1
                count += 1
            else:
                carry = 1
                count += 2
            l -= 1
    
        if carry == 1:
            count += 1
        return count