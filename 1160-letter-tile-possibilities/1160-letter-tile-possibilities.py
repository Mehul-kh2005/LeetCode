class Solution:
    def find_sequences(self,char_count):
        total_count=0

        for i in range(26):
            if char_count[i]==0:
                continue

            total_count+=1
            char_count[i]-=1
            total_count+=self.find_sequences(char_count)
            char_count[i]+=1

        return total_count

    def numTilePossibilities(self, tiles: str) -> int:
        char_count=[0]*26
        for char in tiles:
            char_count[ord(char)-ord("A")]+=1
        
        return self.find_sequences(char_count)