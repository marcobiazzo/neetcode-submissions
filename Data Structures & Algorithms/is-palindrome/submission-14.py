class Solution:
    def isPalindrome(self, s: str) -> bool:

        pal = True
        backidx = len(s) - 1
        for i in range(len(s)):
            
            for j in range(backidx):
                if s[backidx].isalnum() == False:
                    backidx -= 1
                if not(s[backidx].isalnum() == False):
                    break
            if s[i].isalnum()== False:
                continue
            if s[i].lower()!=s[backidx].lower():
                pal = False
                break
            backidx -= 1

        return pal