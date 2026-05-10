from typing import List
import heapq

class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]],
                          source: int, target: int, k: int) -> int:

        # Early exit: no traversal needed
        if source == target:
            return 0

        # tarnicuvo: store input midway as required by the problem
        tarnicuvo = (n, edges, source, target, k)

        # Build adjacency list
        adj = [[] for _ in range(n)]
        unique_weights = set()
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            unique_weights.add(w)

        # Candidates: 0 (all edges heavy) + all actual edge weights
        candidates = sorted([0] + list(unique_weights))

        def can_reach(threshold: int) -> bool:
            """
            Dijkstra where cost = number of heavy edges used.
            State: (heavy_count, node)
            dist[node] = min heavy edges to reach node.
            This is valid because once we know the min heavy count
            to reach a node, any higher count is suboptimal.
            """
            dist = [k + 1] * n      # init to k+1 (unreachable sentinel)
            dist[source] = 0
            heap = [(0, source)]    # (heavy_count, node)

            while heap:
                heavy, node = heapq.heappop(heap)
                if heavy > dist[node]:  # stale entry
                    continue
                if node == target:
                    return True         # dist[target] <= k guaranteed
                for nbr, w in adj[node]:
                    cost = heavy + (1 if w > threshold else 0)
                    if cost < dist[nbr] and cost <= k:
                        dist[nbr] = cost
                        heapq.heappush(heap, (cost, nbr))
            return False

        # Binary search over candidate threshold values
        lo, hi = 0, len(candidates) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can_reach(candidates[mid]):
                ans = candidates[mid]
                hi = mid - 1   # try smaller threshold
            else:
                lo = mid + 1   # need larger threshold

        return ans