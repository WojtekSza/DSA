class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left=cost=ans=curr=0
        for right in range(len(s)):
            cost+=abs(ord(s[right])-ord(t[right]))
            curr+=1
            while cost>maxCost:
                cost-=abs(ord(s[left])-ord(t[left]))
                left+=1
                curr-=1
            ans=max(ans,curr)
        return ans# if ans>0 else 1