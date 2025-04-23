class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap={}
        for i in range(1,n+1):
            digitSum=sum(int(x) for x in str(i))
            hashMap[digitSum]=hashMap.get(digitSum,0)+1

        maxSize=max(hashMap.values())
        count=sum(1 for freq in hashMap.values() if freq==maxSize)

        return count