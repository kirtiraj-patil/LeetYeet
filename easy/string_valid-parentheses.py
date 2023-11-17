class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in list(brac.values()):
                stack.append(i)
            elif len(stack) != 0 and brac[i] == stack.pop():
                continue
            else:
                return False

        return len(stack) == 0
