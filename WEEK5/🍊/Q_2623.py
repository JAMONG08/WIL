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



'''
    2. 각각의 약수를 구함 - http://www.tcpschool.com/codingmath/common
'''
cd = {}
cd[2] = 0
total = 1

def GCD(n, end=0):
    global total
    key = 2
    while True:
        if(n < key):
            return
        
        if((key == 2 or key % 2 != 0) and n % key == 0):
            if(end == 0):
                cd[key] += 1
            else:
                if(cd[key] > 0):
                    cd[key] -= 1
                    total *= key
            n //= key
        else:
            key += 1
            if not key in cd:
                cd[key] = 0


nums = [int(str) for str in input().split()]
if(nums[0] <= nums[1]):
    GCD(nums[1])
    GCD(nums[0], 1)
else:
    GCD(nums[0])
    GCD(nums[1], 1)

print(total)
'''
    동적변수 : locals()['cd{}'.format(k)] = {}
'''