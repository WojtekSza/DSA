from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=ans=curr=0
        items=defaultdict(int)
        for i in range(len(nums)):
            items[nums[i]]+=1
            curr+=nums[i]
            while items[nums[i]]>1:
                items[nums[left]]-=1
                curr-=nums[left]
                left+=1
            ans=max(ans,curr)
        return ans
