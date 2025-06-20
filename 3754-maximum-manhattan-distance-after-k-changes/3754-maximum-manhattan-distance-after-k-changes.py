class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        latitude=0
        longitude=0
        ans=0

        for i in range(len(s)):
            if s[i]=='N':
                latitude+=1

            elif s[i]=='S':
                latitude-=1

            elif s[i]=='E':
                longitude+=1

            elif s[i]=='W':
                longitude-=1

            ans=max(ans,min(abs(latitude)+abs(longitude)+k*2,i+1))

        return ans