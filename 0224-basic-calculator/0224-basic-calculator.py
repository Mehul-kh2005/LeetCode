class Solution:
    def calculate(self, s: str) -> int:
        num=0
        sign=1
        result=0
        stack=[]

        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)

            elif ch in "+-":
                result+=num*sign
                sign=-1 if ch=="-" else 1
                num=0

            elif ch=="(":
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1

            elif ch==")":
                result+=num*sign
                result*=stack.pop()
                result+=stack.pop()
                num=0

        return result+(num*sign)