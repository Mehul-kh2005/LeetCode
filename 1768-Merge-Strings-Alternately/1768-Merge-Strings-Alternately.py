class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        len1 = len(word1)
        len2 = len(word2)

        i = j = 0

        while i < len1 and j < len2:
            result.append(word1[i])
            result.append(word2[i])
            i+=1
            j+=1
           
        if i < len1:
            result.append(word1[i:])
        if j < len2:
            result.append(word2[j:])
        return ''.join(result)