class Solution:
    def possibleStringCount(self, word: str) -> int:
        n=len(word)
        result=1

        for i in range(1,n):
            if word[i]==word[i-1]:
                result+=1

        return result