class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right=len(arr)-1
        while right>0 and arr[right]>=arr[right-1]:
            right-=1

        left,ans=0,right
        
        while left<right and (left==0 or arr[left]>=arr[left-1]):
            while right<len(arr) and arr[left]>arr[right]:
                right+=1

            ans=min(ans,right-left-1)
            left+=1

        return ans