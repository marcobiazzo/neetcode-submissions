class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ","").lower()
        s = "".join(c for c in s if c.isalnum())
        pal = True
        for i in range(len(s)):
            if s[i]!=s[-i-1]:
                pal = False
                break

        return pal