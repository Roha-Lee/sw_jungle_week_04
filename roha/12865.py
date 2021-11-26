import sys 
def max_value_knapsac(num_stuff, weights, values, target_weight):
    DP = [[0] * (target_weight + 1) for _ in range(num_stuff + 1)]

    for r in range(1, num_stuff+1):
        for c in range(1, target_weight+1):
            DP[r][c] = DP[r-1][c]
            if c >= weights[r-1]:
                DP[r][c] = max(DP[r][c], DP[r-1][c-weights[r-1]] + values[r-1])

    return DP[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.readline
    num_stuff, target_weight = map(int, input().split())
    
    weights = []
    values = []
    for _ in range(num_stuff):
        weight, value = map(int, input().split())
        values.append(value)
        weights.append(weight)
    print(max_value_knapsac(num_stuff, weights, values, target_weight))