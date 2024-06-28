from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        ans=left=summ=0
        for i in range(len(nums)):
            freq[nums[i]]+=1
            summ+=1
            while freq[nums[i]]>k:
                freq[nums[left]]-=1
                summ-=1
                left+=1
            if freq[nums[i]]<=k:
                ans=max(ans,summ)
        return ans