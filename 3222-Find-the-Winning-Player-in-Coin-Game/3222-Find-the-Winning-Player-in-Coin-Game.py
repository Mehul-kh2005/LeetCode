class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        moves = 0

        while True:
            if x >= 1 and y >= 4:
                x -= 1
                y -= 4
                moves += 1

            elif x >= 3 and y >= 4:
                x -= 3
                y -= 4
                moves += 1
                
            else:
                break 

        if moves % 2 == 1:
            return "Alice"
        else:
            return "Bob"