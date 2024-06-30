class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        s = []
        ans = [0] * len(heights)
        for i in range(len(heights)):
            while s and heights[s[-1]] <= heights[i]:
                ans[s.pop()] += 1
            if s:
                ans[s[-1]] += 1
            s.append(i)
        return ans