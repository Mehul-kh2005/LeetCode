class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(num):
            digits=[]
            while num:
                digits.append(num%k)
                num//=k

            return digits==digits[::-1]

        left,count,result=1,0,0

        while count<n:
            right=left*10

            for parity in [0,1]:
                for x in range(left,right):
                    if count==n:
                        break

                    digit=x//10 if parity==0 else x

                    while x:
                        digit=digit*10+x%10
                        x//=10

                    if isPalindrome(digit):
                        count+=1
                        result+=digit

            left=right

        return result        