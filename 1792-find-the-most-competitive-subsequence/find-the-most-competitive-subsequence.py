class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
            st = []
            for idx, num in enumerate(nums):
                if not st:
                    st.append(num)
                else:
                    # pop element from st if last element is greater than the current element
                    # and also I have enough elements left such that I can have list of size k
                    while st and st[-1] > num and (len(st)-1 + len(nums)-idx >= k):
                        st.pop()
                    if len(st) < k:
                        st.append(num)
            return st