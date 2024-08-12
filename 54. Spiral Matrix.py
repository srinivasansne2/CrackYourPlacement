class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        count, direction = m * n, 1
        i, j, result = 0, -1, []

        while len(result) != count:
            for _ in range(n):
                j += direction
                result.append(matrix[i][j])
            m -= 1

            for _ in range(m):
                i += direction
                result.append(matrix[i][j])
            n -= 1

            direction *= -1
        
        return result