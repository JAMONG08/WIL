import sys
input = sys.stdin.readline

# n: 세로(행), m: 가로(열), r: 도는 횟수
n,m,r = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
    	# x, y 는 돌려지는 배열중 가장 첫번째 배열 인덱스 -> (1, 1)
        x, y = i, i
        temp = data[x][y]  
                      
        # 안쪽까지 계속 돌아야하기 때문에 n-i랑 m-i까지로 범위설정 -> 안쪽으로 들어가면 맨 바깥보다 작아야져 하니까
        for j in range(i + 1, n - i):  #왼쪽
            x = j
            prev = data[x][y]
            data[x][y] = temp
            temp = prev

        for j in range(i + 1, m - i):  #아래
            y = j
            prev = data[x][y]
            data[x][y] = temp
            temp = prev

        for j in range(i + 1, n - i):  #오른쪽
            x = n - j - 1
            prev = data[x][y]
            data[x][y] = temp
            temp = prev

        for j in range(i + 1, m - i):  #위
            y = m - j -1
            prev = data[x][y]
            data[x][y] = temp
            temp = prev

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()


# 참고 : https://resilient-923.tistory.com/303