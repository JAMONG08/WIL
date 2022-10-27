# 1402 : 거꾸로 출력하기 3
'''
key : 배열의 크기
nums : 입력받은 숫자들
'''
key = int(input()) - 1 
nums = input().split()

for i in range(key, -1, -1):
    print(nums[i], end=' ')