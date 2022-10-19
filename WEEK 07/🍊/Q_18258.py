# 큐 2

'''
queue = []

def push(n):
    global queue
    return queue.append(n)

def pop():
    global queue
    if len(queue) <= 0:
        return -1
    else: return queue.pop(0)

def size():
    global queue
    return len(queue)

def empty():
    global queue
    if len(queue) > 0:
        return 0
    else: return 1

def front():
    global queue
    if len(queue) <= 0:
        return -1
    else: return queue[0]

def back():
    global queue
    if len(queue) <= 0:
        return -1
    else: return queue[(len(queue)-1)]


functions = {'push': push,
             'pop': pop,
             'size': size,
             'empty': empty,
             'front': front,
             'back': back,
            }


num = int(input())
answer = []

for i in range(num):
    command = input().split()
    if command[0] == 'push':
        functions[command[0]](int(command[1]))
    else: 
        answer.append(functions[command[0]]())

for i in answer:
    print(i)


참고 : https://www.bangseongbeom.com/python-switch-case.html
'''


from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque([])

for _ in range(n):
    query = input().split()
    if query[0] == 'push':
            q.append(query[1])
    elif query[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif query[0] == 'size':
        print(len(q))
    elif query[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif query[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif query[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)

'''
    https://puleugo.tistory.com/42
    https://chaewonkong.github.io/posts/python-deque.html
'''