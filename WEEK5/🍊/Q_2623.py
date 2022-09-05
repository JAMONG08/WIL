### 2641 : 최대공약수 구하기
'''
    최대공약수 수학 : https://mathbang.net/202

    1. 그냥 둘 한꺼번에 나눠서 구함 - https://mathbang.net/202
'''

nums = [int(str) for str in input().split()]
if(nums[0] <= nums[1]):
    end = nums[0]
else:
    end = nums[1]

min = 0
for i in range(1, end+1):
    if(nums[0] % i == 0 and nums[1] % i == 0):
        min = i

print(min)
'''
    리스트의 모든 문자열을 int 값으로 변경 : 
        https://hbesthee.tistory.com/1727
'''
