class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def compareVersionHelper(string:str,idx:int)-> List[int]:
            num=0
            while idx<len(string):
                if string[idx]==".":
                    break
                num=num*10 + int(string[idx])
                idx+=1
            return [num,idx+1]


        i=j=0
        while (i<len(version1) or j<len(version2)):
            value1,i=compareVersionHelper(version1,i)
            value2,j=compareVersionHelper(version2,j)

            if value1>value2:
                return 1
            elif value1<value2:
                return -1
        return 0