class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distX=abs(z-x)
        distY=abs(z-y)

        if distX<distY:
            return 1

        elif distX>distY:
            return 2
            
        else:
            return 0