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
    +)
    a = input(); for i in a: // range, len 안써도 됨
    배열 음수 인덱스
'''