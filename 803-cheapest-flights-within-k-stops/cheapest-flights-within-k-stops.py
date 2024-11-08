class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        inf=float('inf')

        dist=[inf]*n

        dist[src]=0

        for _ in range(k+1):

            back=dist.copy()

            for f, t, p in flights:

                dist[t]=min(dist[t],back[f]+p)

        return -1 if dist[dst]==inf else dist[dst]


        