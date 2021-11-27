from sys import stdin

N, K = map(int, stdin.readline().split())

arr = [int(stdin.readline()) for _ in range(N)]
share, remainder = float('inf'), float('inf')
dividend = K
ans = 0

while remainder:
    share, remainder = float('inf'), float('inf')
    pf, pl = 0, N-1
    while pl >= pf:
        pc = (pf+pl)//2
        crrQ = dividend//arr[pc]
        if crrQ == 0 or crrQ > share:
            pl = pc-1
        
        elif crrQ < share:
            pf = pc+1
            share = crrQ
            remainder = dividend % arr[pc]
    ans += share
    dividend = remainder

print(ans)