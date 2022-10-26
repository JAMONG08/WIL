# 다음 순열

N = int(input())
input_array = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if input_array[i-1] < input_array[i]:
        for j in range(N-1, 0, -1):
            if input_array[i-1] < input_array[j]:
                input_array[i-1], input_array[j] = input_array[j], input_array[i-1]
                input_array = input_array[:i] + sorted(input_array[i:])
                print(*input_array)
                exit()

print(-1)

'''
https://jminie.tistory.com/76
https://ji-gwang.tistory.com/262
'''





'''
n = int(input())
goal = list(map(int, input().split(' ')))
flag = False
pList = []
result = ''

def combi():
    global n, result, flag

    if(len(pList) == n):
        if(flag):
            result = ' '.join(map(str, pList))
            flag = False
            return

        if(goal == pList):
            flag = True

    for i in range(1, n+1):
        if i not in pList:
            pList.append(i)
            combi()
            pList.pop()

    if(flag == True):
        result = -1

combi()
print(result)
'''