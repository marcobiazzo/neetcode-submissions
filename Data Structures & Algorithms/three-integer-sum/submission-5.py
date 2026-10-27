class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        d = Counter(nums) # this dictonary will be number - > count in nums, we will look it up when a couple i, j is fixed and see if the number is in the dic, if yes and the count is >1 then we put it in the result, then we eliminate the doubles in the result
        seen = set()
        for i,_ in enumerate(nums):
            for j,_ in enumerate(nums):

                current_gap = -(nums[i] + nums[j])

                # allora adesso ci sono diversi casi 
                # caso 1: tutti e tre i numeri diversi
                if (current_gap in d) and ((nums[i]!=nums[j]) and (nums[i]!=current_gap) and (nums[j]!=current_gap)):
                    seen.add(tuple(sorted([nums[i], nums[j], current_gap])))
                # caso 2: current gap = nums i different form numj
                if (current_gap in d) and ((current_gap==nums[i]) and (current_gap!=nums[j])):
                    if(d[current_gap]>1):
                        seen.add(tuple(sorted([nums[i], nums[j], current_gap])))

                # caso 3: current gap = nums j different from num i
                if (current_gap in d) and ((current_gap!=nums[i]) and (current_gap==nums[j])):
                    if(d[current_gap]>1):
                        seen.add(tuple(sorted([nums[i], nums[j], current_gap])))

                # caso 4: current gap = nums j = num i - possibile? no devono sommare zero, invece si quando e' zero
                if (current_gap in d) and ((current_gap==nums[i]) and (current_gap==nums[j])):
                    if(d[current_gap]>2):
                        seen.add(tuple(sorted([nums[i], nums[j], current_gap])))

                # ok now we need to find a smart way to remove the duplicates

        return [list(t) for t in seen]
