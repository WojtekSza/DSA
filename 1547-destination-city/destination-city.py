from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        routes=defaultdict(int)
        for i in paths:
            routes[i[0]]+=1
            routes[i[1]]-=1
        for city,count in routes.items():
            if count==-1:
                return city
        