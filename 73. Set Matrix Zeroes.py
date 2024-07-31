class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        index =[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    index.append((i,j))
        for i,j in index:
            for k in range(n):
                matrix[i][k] = 0
            for l in range(m):
                matrix[l][j] = 0