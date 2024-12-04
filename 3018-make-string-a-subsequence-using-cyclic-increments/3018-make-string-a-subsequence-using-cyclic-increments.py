class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j=0
        for i in range(len(str1)):
            next_char = chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a'))
            if str1[i]==str2[j] or next_char==str2[j]:
                j+=1

            if j==len(str2):
                return True

        return False