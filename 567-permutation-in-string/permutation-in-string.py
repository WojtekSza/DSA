from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict=Counter(s1)
        start=0
        end=len(s1)
        while end<=len(s2):
            s1dict_check=s1dict.copy()
            word=s2[start:end]
            for i in word:
                if i in s1dict_check:
                    s1dict_check[i]-=1
            check=set(s1dict_check.values())
            if 0 in check and len(check)==1:
                return True
            end+=1
            start+=1
        return False