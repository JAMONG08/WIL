num = int(input())

# 1. for문 사용
sum_f = 0

for i in range(1, num+1):
  if(i%2 == 0):
    sum_f += i
  
print(sum_f, end="\n")  
  
  
# 2. while문 사용
sum_w = 0

i = 0
while(i < num):
  i = i + 1
  if(i%2 == 1):
    continue
  else:
    sum_w += i   

print(sum_w)