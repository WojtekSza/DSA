from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_counts=current_sum=0
        freq=defaultdict(int)
        for num in nums:
            current_sum+=num
            if current_sum==goal:
                total_counts+=1
            if current_sum - goal in freq:
                total_counts+=freq[current_sum - goal]
            freq[current_sum]+=1
        return total_counts