class Solution(object):
    def kLengthApart(self, nums, k):
        distance = 0
        found = False
        
        for num in nums:
            if num == 1:
                if distance <= k and found:
                    return False 
                
                found = True
                distance = 0

            distance += 1

        return True