class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        shift_accum=[0]*(n+1)

        for start,end,direction in shifts:
            if direction==1:
                shift_accum[start]+=1
                shift_accum[end+1]-=1

            else:
                shift_accum[start]-=1
                shift_accum[end+1]+=1

        net_shifts=[0]*n
        cumulative=0

        for i in range(n):
            cumulative+=shift_accum[i]
            net_shifts[i]=cumulative

        result=[]
        for i in range(n):
            original_pos=ord(s[i])-ord('a')
            new_pos=(original_pos+net_shifts[i])%26
            result.append(chr(new_pos+ord('a')))

        return "".join(result)