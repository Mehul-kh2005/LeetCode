class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        nums=[0]*100
        result=0

        for x,y in dominoes:
            val=10*x+y if x>=y else 10*y+x
            result+=nums[val]
            nums[val]+=1

        return result