## TLE!

import sys 
from collections import Counter
# suffix array를 빠르게 만드는 알고리즘 (Manber-Myers 알고리즘)
# https://www.youtube.com/watch?v=_TUeAdu-U_k
# 현재 -> O(nlog^2(n)) / optimal -> O(nlog(n)) 

# def get_rank(pairs):
#     cntr = Counter(pairs)
#     cntr_keys = sorted(cntr.keys())
#     value_to_rank = {elem : idx for idx, elem in enumerate(cntr_keys)}
#     return [value_to_rank[pair] for pair in pairs]

# def is_all_unique(n, pairs):
#     pairs = set(pairs)
#     return n == len(pairs)

# def generate_suffix_array(word):
#     ascii_word = [ord(letter) for letter in word]
    
#     pairs = []
#     for i in range(1, len(ascii_word)):
#         pairs.append((ascii_word[i-1], ascii_word[i]))
#     pairs.append((ascii_word[i], -1))
    
#     while not is_all_unique(len(word), pairs):
#         next_ranks = get_rank(pairs)
#         pairs = []
#         for i in range(1, len(next_ranks)):
#             pairs.append((next_ranks[i-1], next_ranks[i]))
#         pairs.append((next_ranks[i], -1))
    
#     suffix_array_inv = get_rank(pairs) 
#     suffix_array = [0] * len(word)

#     for i in range(len(word)):
#         suffix_array[suffix_array_inv[i]] = i
    
#     return suffix_array, suffix_array_inv

def generate_suffix_array(word):
    word_len = len(word)
    sa = [i for i in range(word_len)]
    rank = [ord(i) for i in word]
    tmp = [0] * word_len
    def f(x): return rank[x] if x < word_len else -1
    t = 1
    while t <= word_len:
        sa.sort(key=lambda x: (f(x), f(x + t)))
        p = 0
        tmp[sa[0]] = 0

        for i in range(1, word_len):
            if f(sa[i - 1]) != f(sa[i]) or f(sa[i - 1] + t) != f(sa[i] + t):
                p += 1
            tmp[sa[i]] = p
        # print(sa, rank, tmp)
        rank = tmp[:]
        t <<= 1
    # print(rank)
    for i in range(word_len):
        rank[sa[i]] = i
    # print(rank)
    return sa, rank
# LCP array 만드는 알고리즘 
# http://alumni.cs.ucr.edu/~rakthant/cs234/01_KLAAP_Linear%20time%20LCP.PDF
def generate_lcp_array(suff_arr, suff_arr_inv, user_input):
    n = len(suff_arr)
    lcp_arr = [0] * n
    height = 0
    split_idx = user_input.index("$")
    for i in range(n):
        if suff_arr_inv[i] > 0:
            k = suff_arr[suff_arr_inv[i]-1]
            if (i + height < split_idx and k + height > split_idx) or (i + height > split_idx and k + height < split_idx):
                while i + height < n and k + height < n and user_input[i+height] == user_input[k+height]:
                    height += 1
                lcp_arr[suff_arr_inv[i]] = height
                if height > 0:
                    height -= 1
    return lcp_arr

if __name__ == '__main__':
    input = sys.stdin.readline
    user_input = input().rstrip() + '$' + input().rstrip()

    suff_arr, suff_arr_inv = generate_suffix_array(user_input)
    lcp_arr = generate_lcp_array(suff_arr, suff_arr_inv, user_input)
    
    max_val = max(lcp_arr)
    idx = lcp_arr.index(max_val)
    print(max_val)
    print(user_input[suff_arr[idx-1]:])
    