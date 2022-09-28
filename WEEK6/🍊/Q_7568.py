# 공통문제 백준_덩치

# ME
'''
person = int(input())

height = []
weight = []
rank = []

for i in range(0, person):
    nums = [int(str) for str in input().split()]
    height.append(nums[0])
    weight.append(nums[1])

def compare(key):
    global height, weight, rank

    rank.append(1)

    for i in range(0, person):
        if(key == i):
            continue

        if(height[key] < height[i] and weight[key] < weight[i]):
            rank[key] += 1

for i in range(0, person):
    compare(i)
'''


# OTHER
person = int(input())

list = []

for i in range(0, person):
    w, h = map(int, input().split())
    list.append([w, h])

for i in range(person):
    rank = 1

    for j in range(person):
        if(list[i][0] < list[j][0] and list[i][1] < list[j][1]):
            rank += 1

    print(rank, end=' ')


'''
    1. 사람수와 몸무게,키 입력받기
    2. 비교하는 함수 만들기
    3. 함수 이요해서 출력하기

    참고 : https://hei-jayden.tistory.com/49
'''