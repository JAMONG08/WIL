### 1912 : (재귀함수) 팩토리얼 계산
num = int(input())
sum = 1

def factorial(num):
    if(num > 1):
        global sum
        sum *= num
        factorial(num-1)
    else:
        print(sum)

factorial(num)


### OTHER
import math
a = int(input('팩토리얼을 구할 숫자를 입력하세요 : '))
print(math.factorial(a))