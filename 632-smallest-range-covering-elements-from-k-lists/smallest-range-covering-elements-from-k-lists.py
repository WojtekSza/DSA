class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
      
        curr_max = float('-inf')
        for i in range(len(nums)):
            heappush(heap,[nums[i][0], i, 0])
            curr_max = max(curr_max,nums[i][0])
        
        best_max =  curr_max
        best_min = heap[0][0]
        while len(heap) == len(nums):
            val, i, j = heappop(heap)
            if j+1 >= len(nums[i]):
                continue
            next_val = nums[i][j+1]
            heappush(heap, [next_val,i,j+1])
            curr_min = heap[0][0]
            curr_max = max(curr_max,next_val)
            if curr_max - curr_min < best_max - best_min:
                best_max = curr_max
                best_min = curr_min
        return [best_min, best_max]
            
        
        
#get min and max for first element of each array
# heap? OF size k
# [value, i,j]
# pop it, increase i to j+1
# i[j+1], check if its max, then compar
#