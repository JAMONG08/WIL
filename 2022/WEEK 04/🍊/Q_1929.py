### 1929 : (재귀함수) 우박수 (3n+1) (reverse)
num = int(input())
stack = []

def reverse(num):
    stack.append(num)

    if(num != 1):
        if(num % 2 != 0):
            num = 3 * num + 1
        else:
            num //= 2
        reverse(num)

    print(stack.pop())

reverse(num)

'''
    스택과 재귀함수의 콜라보

    맨 마지막 1을 표시하기 위해 else문에 print(1)
    7번 문제에서 걸림 -> if문 1 검사 추가

    -> 수정
    reverse 함수 호출되는 횟수만큼 스택의 값이 없어서
    에러뜨기 때문에 함수 호출하면 무조건 스택에 값을
    넣는 방식으로 변경

    // : 정수만 구하는 나눗셈
    / : 소수까지 구하는 나눗셈
'''