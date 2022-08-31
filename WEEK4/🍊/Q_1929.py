### 1929 : (재귀함수) 우박수 (3n+1) (reverse)
num = int(input())
stack = []

def reverse(num):
    if(num != 1):
        stack.append(num)

        if(num % 2 != 0):
            num = 3 * num + 1
        else:
            num //= 2
        reverse(num)

    else:
        print(1)

    print(stack.pop())

reverse(num)

'''
    스택과 재귀함수의 콜라보
    맨 마지막 1을 표시하기 위해 else문에 print(1)
    7번 문제에서 걸림 -> if문 1 검사 추가
    // : 정수만 구하는 나눗셈
'''