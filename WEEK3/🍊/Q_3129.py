### 3129 : 올바른 괄호 2
# ME ''' START
bracket = list(input())
length = len(bracket)
check = []
flag = False

if length % 2 == 0:
    for i in range(length):
        cLen = len(check)

        if (i == 0 or cLen == 0) and bracket[i] == ')':
            flag = False
            break

        if bracket[i] == '(':
            check.append('(')
        elif bracket[i] == ')':
            del check[cLen-1]
            flag = True

if(flag == True and len(check) == 0):
    print('good')
else:
    print('bad')

'''
bracket : 괄호입력아서 만들어진 배열
length : 괄호배열의 크기
check : 괄호 체크용 스택 배열
flag : 
    1. 괄호배열가 2의 배수가 아니거나
    2. 맨처음 괄호가 닫힌 괄호_)일 경우거나
    3. 괄호 체크용 스택 배열의 크기가 0인데 닫힌 괄호_)일 경우
    검사 중간에 빠져나오기 위한 신호기
'''


# OTHER ''' START
# https://m.blog.naver.com/luvwithcat/221878016515
a = input()
stack = []

for i in a:
    stack.append(i)
    if len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':
        stack.pop()
        stack.pop()

if stack:
    print('bad')
else:
    print('good')

'''
    Plus+_)
    a = input(); for i in a: // range, len 안써도 됨
    배열 음수 인덱스
'''