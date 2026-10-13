class Solution:

    def encode(self, strs: List[str]) -> str:

        # lets think about how do encode. So for each char we have a correspondend iuni code right?

        # actually before thinking fancy - there is a super simple way

        res = ""
        for s in strs:
            res += s + "\x1f"
        return res

    def decode(self, s: str) -> List[str]:

        idx = 0
        res = []
        for i, c in enumerate(s):
            if c == '\x1f':
                res.append(s[idx:i])
                if i!=len(s)-1:
                    idx = i+1
        
        return res