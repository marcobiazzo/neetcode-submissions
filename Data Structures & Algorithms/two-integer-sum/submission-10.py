class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # I am going to write ugly code

        # here we create the dic
        dic = {}
        for i, n in enumerate(nums):
            dic[n]= i

        # here we iterate on the dic and see if there is a difference to the target present 
        for i, n in enumerate(nums):
            if dic.get(target - n, 0)!=0 and dic.get(target - n,0)!=i:
                return [i, dic.get(target - n, 0)]   