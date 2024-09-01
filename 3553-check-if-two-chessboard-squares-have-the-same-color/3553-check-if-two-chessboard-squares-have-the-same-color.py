class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        dict1={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
        
        s1="black" if (dict1[coordinate1[0]]+int(coordinate1[1]))%2==0 else "white"
        s2="black" if (dict1[coordinate2[0]]+int(coordinate2[1]))%2==0 else "white"

        if s1==s2:
            return True
        else:
            return False