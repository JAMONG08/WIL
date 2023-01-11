# 전화번호 목록
import sys
N1 = int(input())
A = []

for i in range(0, N1):
    N2 = int(input())
    ph1 = list(map(str, input()))
    l = len(ph1)
    A.append('YES')

    for j in range(1, N2):
        ph2 = list(map(str, input()))
        if ph1 == ph2[:l]:
            A[i] = 'NO'
            break

print(*A, sep='\n')

'''
https://velog.io/@injoon2019/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-5052-%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''