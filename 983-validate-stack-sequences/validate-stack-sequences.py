class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        step=0
        curr=[]
        for i in range(len(pushed)):
            curr.append(pushed[i])
            while curr and  curr[-1]==popped[step]:
                curr.pop()
                step+=1
        if len(curr)==0:
            return True
        else:
            return False
        