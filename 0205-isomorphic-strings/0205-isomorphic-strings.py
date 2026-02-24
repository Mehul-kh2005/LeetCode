class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        arr1=[0]*256
        arr2=[0]*256

        for i in range(0,len(s)):
            if arr1[ord(s[i])]!=arr2[ord(t[i])]:
                return False

            arr1[ord(s[i])]=i+1
            arr2[ord(t[i])]=i+1

        return True