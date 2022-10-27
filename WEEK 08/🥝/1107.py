
'''
완전탐색 알고리즘
완전탐색은 간단히 가능한 모든 경우의 수를 다 체크해서 정답을 찾는 방법
무식, 직관적이어서 이해하기 쉬움, 가장 확실하며 기초적인 방법.
'''
import sys
input = sys.stdin.readline
N = int(input())  # 이동하려고 하는 채널
M = int(input())  # 고장난 버튼 개수
break_btn= list(map(int, input().split()))  # 고장난 버튼

cnt = abs(100 - N)  # + or - 로 이동할 경우 최댓값(지금 보고 있는 채널은 100번)

# print(cnt)

# 1000000번 돌리는 이유 N의 최대값이 500000 이기때문에 -, + 두가지 방법으로 접근이 가능하기때문에 2배를 곱해준다.
# EX) -, + 두가지 방법으로 접근 : N = 500000 1~499999 + OR 5000001~1000000 -
for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)): 
        # 각 숫자의 버튼이 고장났는지 확인 후 고장 났으면 break
        if int(nums[j]) in break_btn:
            break
        # 고장난 숫자 없이 마지막 자리까지 왔다면 cnt 비교 후 업데이트
        elif j == len(nums) - 1:
            cnt = min(cnt, abs(int(nums) - N)+len(nums)) #(cnt,현재채널에서 목표채널로 가기위한 버튼 클릭 횟수)

print(cnt)
