class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=[0]*26

        for char in word:
            freq[ord(char)-ord("a")]+=1

        freq.sort(reverse=True)
        total_pushes=0

        for i in range(26):
            if freq[i]==0:
                break
            total_pushes+=(i//8+1)*freq[i]

        return total_pushes