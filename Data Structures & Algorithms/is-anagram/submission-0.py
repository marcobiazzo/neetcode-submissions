class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        dic1, dic2 = {},{}
        for l1, l2 in zip(s, t):
 
            dic1[l1]= dic1.get(l1,0) + 1 
            dic2[l2]= dic2.get(l2,0) + 1 
        return dic1 == dic2