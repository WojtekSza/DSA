from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            if node in graph:
                for i in graph[node]:
                    if i not in sub_set:
                        sub_ans.append(i)
                        sub_set.add(i)
                        dfs(i)
        graph=defaultdict(list)
        for x,y in edges:
            graph[y].append(x)
        ans=[]
        for i in range(n):
            sub_ans=[]
            sub_set=set()
            dfs(i)
            sub_ans.sort()
            ans.append(sub_ans)
        return ans

        