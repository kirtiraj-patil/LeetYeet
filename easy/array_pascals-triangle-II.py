class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        if rowIndex == 1:
            res.append([1, 1])
            return res[-1]

        for i in range(2, rowIndex + 2):
            newRow = [1]
            for j in range(0, len(res[-1]) - 1):
                newRow.append(res[-1][j] + res[-1][j + 1])
            newRow.append(1)
            res.append(newRow)

        return res[-1]
