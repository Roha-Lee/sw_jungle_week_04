import sys 
def make_minimum(user_input):
    split_minus = user_input.split('-')
    result = None
    for part in split_minus:
        val = sum(map(int, part.split('+')))
        if result is None:
            result = val
        else:
            result -= val
    return result

if __name__ == '__main__':
    input = sys.stdin.readline
    user_input = input().rstrip()
    print(make_minimum(user_input))


