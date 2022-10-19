#n개의 수를 덧셈과 뺄셈을 이용하여 m이 되는 경우의 수
#첫 번째 줄에 m이 입력된다.
#두 번째 줄에 n이 입력된다. (0<=n<=20) 0rofm
# m을 만들 수 있는 경우의 수를 출력한다. 입력되는 수들은 모두 사용해야 하며 한 번씩만 사용할 수 있다.
# 3개를 입력한다
# 1 -> +1 -1 2가지경우//  -1 => -1 -(-1) //  1 => +1 -1 2가지 경우


goal = int(input())
n = int(input())
cnt = 0

def sumZero(i, num, goal):
    global cnt, n
  
    if(i+1 == n):    #인덱스+1 = 배열수 = 입력받은 원소갯수 = 지금 배열 마지막임
        if(num == goal):    #최종값이 같아야한다 9 num=3 =  6  
            cnt += 1
        return
    sumZero(i+1,in_arr[i+1], goal-num)
    sumZero(i+1,-in_arr[i+1], goal+num)

if(n != 0):
    in_arr = list(map(int,input().split()))
    sumZero(-1,0,goal)

print(cnt)
