# N = 216  
# 0 ~ N 다 확인 : 198 or 207

N = int(input())
result = 0

for i in range(1, N+1):
    number = list(map(int, str(i)))  # []
    result = i + sum(number)
    # java 버전
    # while (number != 0):
    #     sum += number % 10
    #     number /= 10

    if  result == N:
        print(i)
        break

    if  i == N:
        print(0)