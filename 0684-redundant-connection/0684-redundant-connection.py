class DSU:
    def __init__(self, N):
        self.N = N
        self.size = [1] * N
        self.representative = list(range(N))

    def _find(self, node):
        # Returns the ultimate representative of the node.
        if self.representative[node] == node:
            return node
        self.representative[node] = self._find(self.representative[node])
        return self.representative[node]

    def _do_union(self, nodeOne, nodeTwo):
        # Returns true if node nodeOne and nodeTwo belong to different component and update the
        # representatives accordingly, otherwise returns false.
        nodeOne = self._find(nodeOne)
        nodeTwo = self._find(nodeTwo)

        if nodeOne == nodeTwo:
            return False
        else:
            if self.size[nodeOne] > self.size[nodeTwo]:
                self.representative[nodeTwo] = nodeOne
                self.size[nodeOne] += self.size[nodeTwo]
            else:
                self.representative[nodeOne] = nodeTwo
                self.size[nodeTwo] += self.size[nodeOne]
            return True


class Solution:
    def findRedundantConnection(self, edges):
        N = len(edges)

        dsu = DSU(N)
        for edge in edges:
            # If union returns false, we know the nodes are already connected
            # and hence we can return this edge.
            if not dsu._do_union(edge[0] - 1, edge[1] - 1):
                return edge

        return []