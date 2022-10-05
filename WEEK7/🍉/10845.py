# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

#https://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readline
# map(int,sys.stdin.readline().strip().split())
# map(int,sys.stdin.readline().split())

#deque stack queue 입력 append(), appendleft(), 출력 popleft(), pop()


from collections import deque
import sys
n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
   # x = input().split()
    x = sys.stdin.readline().strip().split()
    if x[0] == 'push':
        queue.append(x[1])
    elif x[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            n = queue.popleft()
            print(n)
    elif x[0] == 'size':
        print(len(queue))
    elif x[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else: print(0)
    elif x[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else: print(queue[0])
    elif x[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else: print(queue[-1])