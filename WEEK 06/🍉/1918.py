# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기 n * m 
# 맨 위 왼쪽 기준 흰색/검은색
# 이전/위칸과 색깔이 달라야함

m, n = map(int, input().split()) #끝 인덱스
board = []
for i in range(m):
    board.append(input())

min_cnt = 64
# 8*8 체스판 모양으로 잘라내야함 
for list_i in range(m - 7):
    for list_j in range(n - 7):
        cnt_b = cnt_w = 0
        for i in range(8):
            for j in range(8):
                if((i+j) % 2 == 0):
                    if(board[i][j] != 'W'):
                        cnt_b += 1
                    if(board[i][j] != 'B'):
                        cnt_w += 1
                else:
                    if(board[i][j] != 'B'):
                        cnt_b += 1
                    if(board[i][j] != 'W'):
                        cnt_w += 1
        min_cnt = min(cnt_b, cnt_w,min_cnt)
print(min_cnt)


# m,n=map(int,input().split())
# l=[input() for i in range(m)]
# M=64
# for i in range(m-7):
#     for j in range(n-7):
#         c=0
#         for k in range(8):
#             for t in range(8):
#                 if l[i+k][j+t]=='WB'[(k+t)%2]:
#                     c+=1
#         M=min(c,64-c,M)
# print(M)