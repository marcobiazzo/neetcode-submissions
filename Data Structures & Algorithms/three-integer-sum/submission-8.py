from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        neg = sorted(x for x in d if x < 0)
        pos = sorted(x for x in d if x > 0)
        res = []

        z = d[0]
        if z >= 3:
            res.append([0, 0, 0])
        if z >= 1:                                   # (-p, 0, p)
            for p in pos:
                if -p in d:
                    res.append([-p, 0, p])

        for i, a in enumerate(neg):                  # two negatives + one positive
            for b in neg[i:]:
                if a == b and d[a] < 2:
                    continue
                if -(a + b) in d:
                    res.append([a, b, -(a + b)])

        for i, b in enumerate(pos):                  # one negative + two positives
            for c in pos[i:]:
                if b == c and d[b] < 2:
                    continue
                if -(b + c) in d:
                    res.append([-(b + c), b, c])
        return res