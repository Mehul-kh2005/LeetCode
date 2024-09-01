class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647  
            
        div_operator = chr(47) 
        
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1

        dividend, divisor = abs(dividend), abs(divisor)

        expression = f"{dividend} {div_operator} {divisor}"
        result = eval(expression)
        
        return sign * int(result)