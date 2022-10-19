def gcd(a, b):
    tmp = min(a, b)  # a,b 중 가장 작은 수를 담음

    while (tmp != 0):
        # 최대공약수는 a,b 둘 다 공통으로 나눠져야 함
        if (a % tmp == 0 and b % tmp == 0):
            return tmp

        # 둘 다 공통적으로 나눠지는 수를 찾기 위해 계속 마이너스
        tmp -= 1


a, b = map(int, input().split())  # a,b 에 정수형으로 받기
print(gcd(a, b))