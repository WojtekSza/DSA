class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=curr=ans=0
        vovels={'a','e','i','o','u'}
        for right in range(len(s)):
            if s[right] in vovels:
                curr+=1
            while right-left>k-1:
                if s[left] in vovels:
                    curr-=1
                left+=1
            ans=max(ans,curr)
        return ans