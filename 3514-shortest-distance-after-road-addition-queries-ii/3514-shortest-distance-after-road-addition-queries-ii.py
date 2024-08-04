from sortedcontainers import SortedList

class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        curr = SortedList()
        
        for i in range(n):
            curr.add(i)
            
            
        ans = []
        
        rest = n - 1
        
        for [l,r] in queries:
            locl = curr.bisect(l)
            locr = curr.bisect_left(r)
            
          #  print(locl,locr,curr)
            
            for _ in range(locr-locl):
                curr.pop(locl)
                rest -= 1
                
            ans.append(rest)
            
        return ans