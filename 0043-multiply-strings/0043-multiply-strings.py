class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        lst1=num1.split()
        val1=int("".join(lst1))

        lst1=num2.split()
        val2=int("".join(lst1))
        
        return str(val1*val2)