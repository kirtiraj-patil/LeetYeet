class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                print(i)
                d[i] = 1
            else:
                d[i] = 0

        for i in range(len(s)):
            char = s[i]
            if d[char] == 0:
                return i

        return -1
