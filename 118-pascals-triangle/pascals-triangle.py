from collections import deque
class Solution:
    def generate(self, numRows: int):
        ans=[[1]]
        for i in range(1,numRows):
            if len(ans[i-1])>1:
                sub_ans=deque([])
                for j in range(len(ans[i-1])-1):
                    sub_ans.append(ans[i-1][j]+ans[i-1][j+1])
                sub_ans.appendleft(1)
                sub_ans.append(1)
                ans.append(list(sub_ans))
            else:
                ans.append([1,1])
        return ans