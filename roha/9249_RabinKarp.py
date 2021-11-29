# PASS!
import sys 
from collections import defaultdict
def is_same_str(str1, str2, start1, start2, window_size):
    for w in range(window_size):
        if str1[start1 + w] != str2[start2 + w]:
            return False
    return True


def RabinKarp(word1, word2, ord_word1, ord_word2, window_size, constant):
    q = 713
    m = 26
    
    hash_list = defaultdict(list)
    constant = m ** window_size
    for start_pos in range(len(word1)-window_size+1):
        if start_pos == 0:
            hash_val = 0
            for i in range(window_size):
                hash_val *= m
                hash_val += ord_word1[i]
                hash_val %= q
            hash_list[hash_val].append(0)
        else:
            hash_val *= m
            hash_val -= ord_word1[start_pos-1] * constant
            hash_val += ord_word1[start_pos+window_size-1]
            hash_val %= q
        hash_list[hash_val].append(start_pos)
    
    for start_pos in range(len(word2)-window_size+1):
        if start_pos == 0:
            hash_val = 0
            for i in range(window_size):
                hash_val *= m
                hash_val += ord_word2[i]
                hash_val %= q
        else:
            hash_val *= m
            hash_val -= ord_word2[start_pos-1] * constant
            hash_val += ord_word2[start_pos+window_size-1]
            hash_val %= q
            
        for i in hash_list[hash_val]:
            if is_same_str(word1, word2, i, start_pos, window_size):
                return i


def find_longest_common_substring(word1, word2, ord_word1, ord_word2):
    q = 713
    m = 26
    constants = [1] * 200001
    for i in range(1, 200000):
        constants[i] = constants[i-1] * m % q
    
    left = 1
    right = min(len(word1), len(word2))
    best_window = 0
    best_idx = 0
    while left <= right:
        mid = (left + right) // 2
        idx = RabinKarp(word1, word2, ord_word1, ord_word2, mid, constants[mid])
        if idx is not None:
            left = mid + 1
            best_window = mid
            best_idx = idx
        else:
            right = mid - 1
    return best_window, word1[best_idx:best_idx+best_window]


if __name__ == '__main__':
    input = sys.stdin.readline
    word1 = input().rstrip()
    word2 = input().rstrip()
    ord_word1 = [ord(letter) - ord('a') for letter in word1]
    ord_word2 = [ord(letter) - ord('a') for letter in word2]
    print(*find_longest_common_substring(word1, word2, ord_word1, ord_word2), sep='\n')