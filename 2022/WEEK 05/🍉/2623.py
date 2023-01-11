#두 정수 a , b 를 입력받아서, a , b 의 최대공약수를 출력하시오.
#GCD, Greateast Common Division
#14 o(n)
# 12456 3456
# a, b = map(int, input().split())

# def gcd1(a, b):
#     for i in range(min(a,b), 0, -1):
#         if(a % i == 0 and b % i == 0):
#             break
#     print(i)

# gcd1(a, b)

# 유클리드 호제법 - 수학 정수론 ~~
# a, b = map(int, input().split())
# def gcd2(a, b):
#     return a if a == 0 else gcd2(b%a, a);

# print(gcd2(a,b))

#16 내장함수
# import math
# a, b = map(int, input().split())
# print(math.gcd(a, b))