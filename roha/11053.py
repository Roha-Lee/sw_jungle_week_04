import sys 
from bisect import bisect_left

def LIS(n, sequences):
    stack = [sequences[0]]
    for i in range(1, n):
        if sequences[i] > stack[-1]:
            stack.append(sequences[i])
        else:
            idx = bisect_left(stack, sequences[i])
            stack[idx] = sequences[i]
    return len(stack)


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    sequences = list(map(int, input().split()))
    print(LIS(n, sequences))
