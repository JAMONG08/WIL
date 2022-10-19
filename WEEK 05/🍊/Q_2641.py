### 2641 : 숏다리의 계단 오르기 (Small)
stair = int(input())

result = 0
def upStair(total, flag):
    global result

    flag -= 1

    if stair == 0 : return 0

    if stair - total >= 1 : upStair(total+1, flag)
    if stair - total >= 2 : upStair(total+2, flag)
    if stair - total >= 3 and flag <= 0 : upStair(total+3, flag)

    elif total == stair : result += 1

upStair(0, 0)

print(result)

'''
    https://jlog1016.tistory.com/33
'''