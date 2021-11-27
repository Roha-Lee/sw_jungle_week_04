from sys import stdin

N = int(stdin.readline())

dp = [[0]*(N) for _ in range(N)]
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

for diagonal in range(1, N):
    for row in range(0, N-diagonal):
        column = row + diagonal
        dp[row][column] = float('inf')
        for i in range(row, column):
            dp[row][column] = min(dp[row][column], dp[row][i]+dp[i+1][column]+(arr[row][0]*arr[i][1]*arr[column][1]))

print(dp[0][N-1])