class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans=[0]*26
            for char in word:
                ans[ord(char)-ord('a')]+=1
            return ans

        bmax=[0]*26
        for word in words2:
            for idx,value in enumerate(count(word)):
                bmax[idx]=max(bmax[idx],value)

        result=[]
        for word in words1:
            if all(x>=y for x,y in zip(count(word),bmax)):
                result.append(word)

        return result