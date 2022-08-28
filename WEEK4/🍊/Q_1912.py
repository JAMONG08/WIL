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