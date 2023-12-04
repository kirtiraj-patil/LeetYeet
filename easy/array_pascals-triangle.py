class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res

        res.append([1, 1])
        for i in range(3, numRows + 1):
            newRow = [1]
            for j in range(0, len(res[-1]) - 1):
                newRow.append(res[-1][j] + res[-1][j + 1])
            newRow.append(1)
            res.append(newRow)

        return res
