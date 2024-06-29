class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)):
            stack=[]
            j=i+1
            while j<len(prices):
                if prices[i]-prices[j]>=0:
                        stack.append(prices[i]-prices[j])
                        break
                j+=1
            if stack:
                ans.append(stack[0])
            else:
                ans.append(prices[i])
        return ans

            
        

        