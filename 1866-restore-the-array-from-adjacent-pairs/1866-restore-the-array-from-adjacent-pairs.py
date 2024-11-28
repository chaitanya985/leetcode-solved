class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph=defaultdict(list)

        for u, v in adjacentPairs:

            graph[u].append(v)

            graph[v].append(u)

        start=next(key for key in graph if len(graph[key])==1)

        nums=[]

        visited=set()

        def dfs(node):

            visited.add(node)

            nums.append(node)

            for neighbor in graph[node]:

                if neighbor not in visited:

                    dfs(neighbor)

        dfs(start)

        return nums


        