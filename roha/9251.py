import sys 
def LCS(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    DP = [[0] * (len2+1) for _ in range(len1+1)]
    for r in range(1, len1 + 1):
        for c in range(1, len2 + 1):
            if word1[r-1] == word2[c-1]:
                DP[r][c] = DP[r-1][c-1] + 1
            else:
                DP[r][c] = max(DP[r][c-1], DP[r-1][c])            
    return DP[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    word1 = input().rstrip()
    word2 = input().rstrip()
    print(LCS(word1, word2))