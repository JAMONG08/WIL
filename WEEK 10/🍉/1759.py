#중복없음, 추가되면 들어오지 않음 자음 모음이 추가됐을때 체크 
#최소 모음 한 개, 자음 두 개 
def PW(idx):
    global M, J
    if len(arr) == l and M >= 1 and J >= 2:
        # str(arr)
        print(*arr,sep='')
        # arr.pop()
        return
    
    while idx != n:
        if not chk[idx]:
            char = chars[idx]
            arr.append(char)
            if char in MS:
                M += 1
            else:
                J += 1
            chk[idx] = -1
            PW(idx+1)
            chk[idx] = 0
            a = arr.pop()
            if a in MS:
                M -= 1
            else:
                J -= 1
            idx += 1

l, n = map(int, input().split())
chars = sorted(list(map(str, input().split())))
# 모음들
MS = ['a', 'e', 'i', 'o', 'u']
chk = [0] * n
# 모음 자음 갯수
M = J = 0
arr = []
PW(0)


# 하나의 리스트에서 모든 조합을 계산을 해야 한다면, permutations, combinations을 사용
# 두개 이상의 리스트에서 모든 조합을 계산해야 한다면, product를 사용
# from itertools import product
# from itertools import permutations
# from itertools import combinations
# https://velog.io/@dramatic/Python-permutation-combination-순열과-조합

# import itertools
# import sys

# L, C = map(int, sys.stdin.readline().split(' '))
# m = sorted((sys.stdin.readline().strip().split(' ')))
# comb = list(itertools.combinations(m, L))
# moeum = set(['a', 'e', 'i', 'o', 'u'])

# for c in comb:
#     moeumLen = len(moeum & set(c))
#     if moeumLen >= 1 and L - moeumLen >= 2:
#         print(''.join(c))