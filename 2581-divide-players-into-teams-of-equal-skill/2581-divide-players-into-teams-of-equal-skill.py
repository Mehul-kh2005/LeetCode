import bisect

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sorted_arr=[]
        total_chemistry=0
        for s in skill:
            bisect.insort(sorted_arr,s)
            
        target_sum=sorted_arr[0]+sorted_arr[-1]
        
        for i in range(len(sorted_arr)//2):
            if sorted_arr[i]+sorted_arr[-i-1]!=target_sum:
                return -1
            total_chemistry+=sorted_arr[i]*sorted_arr[-i-1]

        return total_chemistry