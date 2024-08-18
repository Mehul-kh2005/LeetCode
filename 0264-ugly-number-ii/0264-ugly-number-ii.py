class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1] * n
        i2 = i3 = i5 = 0
        
        next_2 = 2
        next_3 = 3
        next_5 = 5
        
        for i in range(1, n):
            ugly_numbers[i] = min(next_2, next_3, next_5)
            
            if ugly_numbers[i] == next_2:
                i2 += 1
                next_2 = ugly_numbers[i2] * 2
            
            if ugly_numbers[i] == next_3:
                i3 += 1
                next_3 = ugly_numbers[i3] * 3
            
            if ugly_numbers[i] == next_5:
                i5 += 1
                next_5 = ugly_numbers[i5] * 5
        
        return ugly_numbers[-1]