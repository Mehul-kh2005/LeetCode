class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        even_count = 1  
        odd_count = 0
        current_sum = 0
        result = 0

        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1
            
            result %= mod
        
        return result