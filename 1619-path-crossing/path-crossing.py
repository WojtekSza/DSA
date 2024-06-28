from collections import defaultdict
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x=0
        y=0
        records=defaultdict(int)
        records[(x,y)]+=1
        for i in path:
            if i=='N':
                y+=1
                records[(x,y)]+=1
            elif i=='S':
                y-=1
                records[(x,y)]+=1
            elif i=='E':
                x+=1
                records[(x,y)]+=1
            elif i=='W':
                x-=1
                records[(x,y)]+=1
        for count in records.values():
            if count>1:
                return True
        return False