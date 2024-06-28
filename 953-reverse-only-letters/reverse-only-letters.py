class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        right=len(s)-1
        ans=[]
        while left<=len(s)-1:
            if s[left].isalpha() and s[right].isalpha():
                ans.append(s[right])
                left+=1
                right-=1
            elif not s[left].isalpha():
                ans.append(s[left])
                left+=1
            elif not s[right].isalpha():
                right-=1
            else:
                ans.append(s[right])
                left+=1
                right-=1
        return "".join(ans)