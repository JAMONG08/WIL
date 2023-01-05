# 모든 순열

n = int(input())
pList = []

def combination():
    global n

    if(len(pList) == n):
        print(*pList)
        return

    for i in range(1, n+1):
        if i not in pList:
            pList.append(i)
            combination()
            pList.pop()

combination()
