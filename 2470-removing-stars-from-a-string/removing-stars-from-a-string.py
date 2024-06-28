class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!='*':
                stack.append(i)
            elif stack and i=='*':
                stack.pop()
        return "".join(stack)
        