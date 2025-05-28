from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        def calc_reach(node, adj_list, num_nodes, max_depth):
            if max_depth < 0:
                return 0 # cant even take starter node
            if max_depth == 0:
                return 1
            
            q = deque([node])
            visited = [False] * num_nodes
            visited[node] = True
            reach = 1
            depth = 0

            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    for nei in adj_list[node]:
                        if not visited[nei]:
                            reach += 1
                            visited[nei] = True
                            q.append(nei)
                depth += 1
                if depth >= max_depth:
                    return reach
            return reach
        
        # find node with best score in tree2
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        adj_list_1 = [[] for _ in range(n1)]
        adj_list_2 = [[] for _ in range(n2)]

        for _from, _to in edges1:
            adj_list_1[_from].append(_to)
            adj_list_1[_to].append(_from)
        for _from, _to in edges2:
            adj_list_2[_from].append(_to)
            adj_list_2[_to].append(_from)

        best_tree_2_reach = 0

        if k >= 1:
            for node in range(n2):
                reach = calc_reach(node, adj_list_2, n2, k - 1)
                if reach >= best_tree_2_reach:
                    best_tree_2_reach = reach
        
        # see reach of reach node in tree 1
        res = [best_tree_2_reach] * n1

        for node in range(n1):
            res[node] += calc_reach(node, adj_list_1, n1, k)

        return res