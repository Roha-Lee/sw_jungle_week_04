from sys import stdin

N, K = map(int, stdin.readline().split())

dp = [[0]*(K+1) for _ in range(N+1)]

item = [[0]]

for _ in range(N):
    item.append(list(map(int, stdin.readline().split())))

item = sorted(item)

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = item[i]
        if j >= w:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
# print(sorted(item))