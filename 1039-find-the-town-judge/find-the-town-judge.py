from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1:
            return 1
        people=defaultdict(int)
        for x,y in trust:
            people[x]-=1
            people[y]+=1
        print(people)
        for i,j in people.items():
            if j==n-1:
                return i
        return -1
        