class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        grid=[[]*n for _ in range(n)]
        for a,b in edges:
            grid[a].append(b)
            grid[b].append(a)

        visited=[False]*n
        complete_components=0

        for vertex in range(n):
            if not visited[vertex]:
                component=[]
                queue=[vertex]
                visited[vertex]=True

                while queue:
                    current=queue.pop(0)
                    component.append(current)

                    for neighbor in grid[current]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor]=True

                is_complete=True
                for node in component:
                    if len(grid[node])!=len(component)-1:
                        is_complete=False
                        break

                if is_complete:
                    complete_components+=1

        return complete_components                            