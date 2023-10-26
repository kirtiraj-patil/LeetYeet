class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longestPalindrome = s[0]
        self.s = s

        if len(s) <= 1:
            return s

        for i in range(len(s)):
            j = len(s) - 1
            if len(self.longestPalindrome) > j - i + 1:
                break
            while j > i:
                res = self.checkPalindrome(i, j)
                if res:
                    if len(self.longestPalindrome) < j - i + 1:
                        self.longestPalindrome = s[i:j+1]
                    break
                else:
                    j -= 1

        return self.longestPalindrome

                
    def checkPalindrome(self, i , j):
        if self.s[i] == self.s[j]:
            if j - i <= 1:
                return True
            else:
                return self.checkPalindrome(i + 1, j - 1)

        return False