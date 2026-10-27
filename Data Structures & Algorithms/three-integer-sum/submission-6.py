from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)                     # value -> how many times it appears
        seen = set()                          # unique triplets as sorted tuples

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):     # each pair once, i != j
                gap = -(nums[i] + nums[j])        # the value k must have

                # copies of gap needed: 1, plus any already used by i or j
                need = 1 + (nums[i] == gap) + (nums[j] == gap)
                if d[gap] >= need:
                    seen.add(tuple(sorted((nums[i], nums[j], gap))))

        return [list(t) for t in seen]