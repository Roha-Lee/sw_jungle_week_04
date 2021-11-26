from sys import stdin

firstLine = list(stdin.readline().rstrip('\n'))
secondLine = list(stdin.readline().rstrip('\n'))

# print(firstLine, secondLine)
dp = []

for i in range(len(firstLine)+1):
    dp.append([0]*((len(secondLine))+1))

for i in range(len(firstLine)):
    for j in range(len(secondLine)):
        if firstLine[i] == secondLine[j]:
            dp[i+1][j+1] = dp[i][j] +1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[len(firstLine)][len(secondLine)])