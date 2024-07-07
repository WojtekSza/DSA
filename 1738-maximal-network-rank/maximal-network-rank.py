from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for x,y in roads:
            graph[x].append(y)
            graph[y].append(x)
        ans=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if i in graph[j]:
                    ans = max(ans, len(graph[i]) + len(graph[j]) - 1)
                else:
                    ans = max(ans, len(graph[i]) + len(graph[j]))
        return ans