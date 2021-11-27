import sys 
def find_new_employees(scores):
    scores = sorted(scores)
    curr_score2 = scores[0][1]
    result = 1
    for _, score2 in scores:
        if score2 < curr_score2:
            result += 1
            curr_score2 = score2
    return result


if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        n  = int(input())
        scores = [tuple(map(int, input().split())) for _ in range(n)]
        print(find_new_employees(scores))
