import sys 
def find_minimum_calculation(rows, cols):
    len_cols = len(cols)
    len_rows = len(rows)
    DP = [[0] * len_rows for _ in range(len_cols)]
    for k in range(1, len_cols):
        for r in range(len_rows-k):
            c = (r + k) 
            DP[r][c] = float('inf')
            for d in range(r, r+k):
                DP[r][c] = min(DP[r][c], DP[r][d] + DP[d+1][c] + rows[r] * cols[d] * cols[c])
    return DP[0][-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    rows = []
    cols = []
    for _ in range(n):
        row, col = map(int, input().split())
        rows.append(row)
        cols.append(col)
    print(find_minimum_calculation(rows, cols))
