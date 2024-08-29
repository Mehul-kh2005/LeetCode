class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)

        adjacency_lists=[[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    adjacency_lists[i].append(j)
                    adjacency_lists[j].append(i)

        num_of_connected_components=0
        visited=[False]*(n)

        def _depth_first_search(stone):
            visited[stone]=True
            for neighbor in adjacency_lists[stone]:
                if not visited[neighbor]:
                    _depth_first_search(neighbor)

        for i in range(n):
            if not visited[i]:
                _depth_first_search(i)
                num_of_connected_components+=1

        return n-num_of_connected_components