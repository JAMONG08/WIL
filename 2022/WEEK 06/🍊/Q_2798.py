#개별문제 백준_블랙잭
n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

def combination(depth, start, sum):
    global m, answer

    if(depth == 3):
        if(sum <= m and answer < sum):
            answer = sum
        return
    
    for i in range(start, n):
        sum+= nums[i]
        combination(depth+1, i+1, sum)
        sum -= nums[i]

combination(0, 0, 0)
print(answer)

'''
    1. 백트래킹
    2. 깊이는 3
    3. 총합은 m 이하

    참고: WEEK1_orange: Q_10974.java
'''