class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq=[]
        if a>0:
            heapq.heappush(pq,(-a,'a'))
        if b>0:
            heapq.heappush(pq,(-b,'b'))
        if c>0:
            heapq.heappush(pq,(-c,'c'))

        result=[]
        while pq:
            count,char=heapq.heappop(pq)
            count=-count
            if len(result)>=2 and result[-1]==char and result[-2]==char:
                if not pq:
                    break
                temp_count,temp_char=heapq.heappop(pq)
                result.append(temp_char)
                if temp_count+1<0:
                    heapq.heappush(pq,(temp_count+1,temp_char))
                heapq.heappush(pq,(-count,char))

            else:
                count-=1
                result.append(char)
                if count>0:
                    heapq.heappush(pq,(-count,char))

        return "".join(result)