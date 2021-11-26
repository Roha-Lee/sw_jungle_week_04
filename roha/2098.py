'''
아래 블로그 글 써주신분 감사합니다!
https://shoark7.github.io/programming/algorithm/introduction-to-tsp-and-solve-with-exhasutive-search
https://shoark7.github.io/programming/algorithm/solve-tsp-with-dynamic-programming
'''
import sys 
def find_path(n, last, visited, DP, distances):
    if visited == ((1<<n) - 1):
        return  distances[last][0] or float('inf')
        
    if DP[last][visited] is not None:
        return DP[last][visited]

    curr_val = float('inf')
    for next in range(n):
        if visited & (1 << next) == 0 and distances[last][next]:
            curr_val = min(curr_val, find_path(n, next, visited | (1<<next), DP, distances) + distances[last][next])

    DP[last][visited] = curr_val

    return curr_val
    

def traveling_salesman_problem(n, distances):
    DP = [[None] * (1<<n) for _ in range(n)]
    return find_path(n, 0, 1, DP, distances)
    

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    distances = [list(map(int, input().split())) for _ in range(n)]
    print(traveling_salesman_problem(n, distances))


