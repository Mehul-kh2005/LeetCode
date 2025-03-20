class Solution:
    def minimumCost(self, n, edges, queries):
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))

        visited = [False] * n

        components = [0] * n
        component_cost = []

        component_id = 0

        for node in range(n):
            if not visited[node]:
                component_cost.append(
                    self._get_component_cost(
                        node, adj_list, visited, components, component_id
                    )
                )
                component_id += 1

        result = []
        for query in queries:
            start, end = query

            if components[start] == components[end]:
                result.append(component_cost[components[start]])
            else:
                result.append(-1)

        return result

    def _get_component_cost(
        self, node, adj_list, visited, components, component_id
    ):

        current_cost = -1

        components[node] = component_id
        visited[node] = True

        for neighbor, weight in adj_list[node]:
            current_cost &= weight
            if not visited[neighbor]:
                current_cost &= self._get_component_cost(
                    neighbor, adj_list, visited, components, component_id
                )

        return current_cost