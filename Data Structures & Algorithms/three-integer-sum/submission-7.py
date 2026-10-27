from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        vals = sorted(d)                      # distinct values, ascending
        res = []
        for x, a in enumerate(vals):
            if a > 0:                         # a <= b <= c and a > 0 -> sum > 0
                break
            for b in vals[x:]:                # b >= a
                c = -(a + b)
                if c < b:                     # keep a <= b <= c: no duplicates, stop early
                    break
                if a == b and d[a] < 2:       # need two copies of a
                    continue
                need = 1 + (a == c) + (b == c)
                if d[c] >= need:
                    res.append([a, b, c])
        return res