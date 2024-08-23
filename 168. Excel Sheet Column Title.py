class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            title = chr(ord('A') + (columnNumber - 1) % 26) + title
            columnNumber = (columnNumber - 1) // 26
        return title