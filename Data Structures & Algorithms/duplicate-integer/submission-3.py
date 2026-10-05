class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dic = {}
        # insert the values in a dic and check if  
        for n in nums:
            
            if n in dic:
                return True
            else:
                dic[n]=''
        return False
    

