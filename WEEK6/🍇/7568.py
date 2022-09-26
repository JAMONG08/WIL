# 이름 (키, 몸무게) 등수
# A	  (55, 185)	    2
# B	  (58, 183)	    2
# C	  (88, 186)	    1
# D	  (60, 175)	    2
# E	  (46, 155)	    5

N = int(input())  # 비교할 사람의 수
dangci = []       # 비교할 사람들의 키, 몸무게
grade = []        # 등수

for i in range(N):
    dangci.append(list(map(int, input().split())))

for i in range(N):
    cnt = 1             # 등수 카운트
    for j in range(N):
        tmp = dangci[i] 
        tmp2 = dangci[j] 
    
        if ((tmp[0] < tmp2[0]) and (tmp[1] < tmp2[1])):
            cnt += 1    # 다음수보다 작으면 등수 +

    grade.append(cnt)   # 각 인덱스별로 등수 넣어줌

for i in range(N):
  print(grade[i], end=' ')