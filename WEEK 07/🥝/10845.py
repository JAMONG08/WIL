
'''
스택 : LIFO
큐 : FIFO
'''
'''

input() vs sys.stdin 승!
참고 : https://developeryuseon.tistory.com/90

input() : 내장함수
input -> 개행문자를 벗겨 내어 -> 문자열로 변환 -> return
참고 : https://docs.python.org/3/library/functions.html#input

sys.stdin : file object
buffer 사용 
참고 : https://docs.python.org/3.10/library/sys.html#sys.stdin

'''
from sys import stdin # sys모듈의 stdin 

n = int(stdin.readline())
queue = []
for i in range(n):
    cmd = stdin.readline().split()

    if cmd[0] == "push":
        queue.append(cmd[1])
        # print(queue)

    elif cmd[0] == "pop":
        if len(queue) == 0: print(-1)
        else: print(queue.pop())

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(0)

    elif cmd[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[0])

    elif cmd[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1])

