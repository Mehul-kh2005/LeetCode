from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]

        for num in nums:
            while stack:
                GCD=gcd(stack[-1],num)

                if GCD==1:
                    break

                num=(stack.pop()*num)//GCD
                
            stack.append(num)

        return stack