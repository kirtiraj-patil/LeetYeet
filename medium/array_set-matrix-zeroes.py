class Solution:
    def __init__(self):
        self.zeroRows = {}
        self.zeroCols = {}

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for rowIndex, row in enumerate(matrix):
            for colIndex, i in enumerate(row):
                if i == 0:
                    self.zeroRows[rowIndex] = True
                    self.zeroCols[colIndex] = True

        # print(self.zeroRows)
        # print(self.zeroCols)
        for rowIndex, row in enumerate(matrix):
            try:
                if self.zeroRows[rowIndex]:
                    for i in range(0, len(row)):
                        matrix[rowIndex][i] = 0
            except KeyError:
                for colIndex, i in enumerate(row):
                    try:
                        if self.zeroCols[colIndex]:
                            matrix[rowIndex][colIndex] = 0
                    except KeyError:
                        continue
