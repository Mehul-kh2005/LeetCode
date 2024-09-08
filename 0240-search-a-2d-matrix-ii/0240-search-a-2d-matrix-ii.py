class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened=sorted([item for sublist in matrix for item in sublist])

        index=bisect.bisect_left(flattened,target)

        if index<len(flattened) and flattened[index]==target:
            return True
        
        return False