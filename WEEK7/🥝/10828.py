
'''
스택 : LIFO
큐 : FIFO
'''

from sys import stdin # sys모듈의 stdin 

n = int(stdin.readline())
stack = []
for i in range(n):
    cmd = stdin.readline().split()
    
    if cmd[0] == "push":
        stack.append(cmd[1])
        print(stack)

    elif cmd[0] == "pop":
        if len(stack) == 0: print(-1)
        else: print(stack.pop())

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        if len(stack) == 0: print(1)
        else: print(0)

    elif cmd[0] == "top":
        if len(stack) == 0: print(-1)
        else: print(stack[len(stack) -1])
