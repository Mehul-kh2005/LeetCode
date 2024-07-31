class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        length = len(flowerbed)

        while i < length:
            # Check if current plot can have a flower
            if flowerbed[i] == 0:
                # Check left and right plots
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    # Place a flower here
                    flowerbed[i] = 1
                    count += 1
                    # Skip next plot to avoid adjacent flowers
                    i += 1
            
            i += 1
        
        return count >= n