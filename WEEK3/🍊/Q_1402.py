# 1402 : 거꾸로 출력하기 3
key = int(input()) - 1
nums = input().split()

for i in range(key, -1, -1):
    print(nums[i], end=' ')