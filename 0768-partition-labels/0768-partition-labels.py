class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurence=[0]*26
        for i in range(len(s)):
            lastOccurence[ord(s[i])-ord('a')]=i

        partitionStart,partitionEnd=0,0
        partitionList=[]
        for i,char in enumerate(s):
            partitionEnd=max(partitionEnd,lastOccurence[ord(char)-ord('a')])
            if i==partitionEnd:
                partitionList.append(i-partitionStart+1)
                partitionStart=i+1

        return partitionList