class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[], ["()"]]
        for i in range(2, n + 1):
            low = 1
            high = i - 1
            d = {}
            while low <= high:
                for string in res[i - 1]:
                    d["(" + string + ")"] = 0
                for string in res[low]:
                    for string2 in res[high]:
                        d[string + string2] = 0
                        d[string2 + string] = 0

                low += 1
                high -= 1

            res.append(list(d.keys()))

        return res[n]
