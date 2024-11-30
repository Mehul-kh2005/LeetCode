class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjacency_matrix=defaultdict(deque)
        in_degree,out_degree=defaultdict(int),defaultdict(int)

        for pair in pairs:
            from_node=pair[0]
            to_node=pair[1]
            adjacency_matrix[from_node].append(to_node)

            out_degree[from_node]+=1
            in_degree[to_node]+=1

        start_node=-1
        for node in out_degree:
            if out_degree[node]==in_degree[node]+1:
                start_node=node
                break

        if start_node==-1:
            start_node=pairs[0][0]
        
        result=[]
        def visit(node):
            while adjacency_matrix[node]:
                next_node=adjacency_matrix[node].popleft()
                visit(next_node)
            result.append(node)

        visit(start_node)
        result.reverse()

        paired_list=[[result[i-1],result[i]] for i in range(1,len(result))]

        return paired_list