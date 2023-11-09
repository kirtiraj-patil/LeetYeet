import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        s = re.sub(r"[^a-zA-Z0-9]+", "", s).lower()
        i = 0
        j = len(s) - 1
        isValid = True
        while i < j:
            if s[i] != s[j]:
                isValid = False
                break
            i += 1
            j -= 1

        return isValid