class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        adj = [[] for _ in range(n)]
        
        for i in range(n - 1):
            adj[i].append(i + 1)
        
        d = [i for i in range(n)]
        ans = []
        
        for query in queries:
            from_node = query[0]
            to_node = query[1]
            adj[from_node].append(to_node)
            
            if d[from_node] + 1 < d[to_node]:
                q = deque([to_node])
                d[to_node] = d[from_node] + 1
                
                while q:
                    v = q.popleft()
                    
                    for next_node in adj[v]:
                        if d[v] + 1 < d[next_node]:
                            d[next_node] = d[v] + 1
                            q.append(next_node)
            
            ans.append(d[-1])
        
        return ans