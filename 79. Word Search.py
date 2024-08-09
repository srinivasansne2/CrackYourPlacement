class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        if len(word) > m*n: 
            return False

        counter = defaultdict(int)
        for i in range(m):
            for j in range(n):
                counter[board[i][j]] += 1

        if counter[word[0]] > counter[word[-1]]: 
            word = word[::-1]
        for char in word:
            if counter[char] == 0: 
                return False
            counter[char] -= 1

        def backtracking(i, j, k):
            res = False
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and k < len(word) and board[i][j] == word[k]:
                if k == len(word) - 1:
                    return True

                temp = board[i][j]
                board[i][j] = ""
                res = backtracking(i + 1, j, k + 1) or \
                    backtracking(i - 1, j, k + 1) or \
                    backtracking(i, j + 1, k + 1) or \
                    backtracking(i, j - 1, k + 1)
                board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(i, j, 0):
                    return True

        return False