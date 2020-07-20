class Solution:
    def rotate(self, matrix) -> None:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i,col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(row):
            matrix[i].reverse()


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
ans = Solution().rotate(matrix)