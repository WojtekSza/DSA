class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        for i in range(len(nums)):
            if i>0 and prefix[i-1]==prefix[-1]-prefix[i]:
                return i
            elif i==0 and prefix[-1]-prefix[i]==0:
                return 0
        return -1