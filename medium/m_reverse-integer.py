class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        positive = x > 0
        num = abs(x)
        res = ""
        while num != 0:
            mod = num % 10
            res += str(mod)
            num //= 10

        res = int(res)
        if res > (2 ** 31) - 1:
            return 0
        elif not positive:
            return -res
        else:
            return res
        