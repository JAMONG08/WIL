# 듣도보도 못한 사람 -> 못듣고 못본 공통 교집합 

import sys

n, m = map(int, input().split())

notListen = set()
notSee = set()

for i in range(n):
    notListen.add(input())

for i in range(m):
    notSee.add(input())

noLS = sorted(list(notListen & notSee))

print(len(noLS))
for name in noLS:
    print(name)
    
# 차집합 a1 - a2
# 교집합 a1 & a2
# 합집합 a1|a2