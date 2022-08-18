# 정수 1~100 중 1개가 입력되었을 때 카운트다운 출력

while(1):
  num = int(input())
  if(num<1 or num>100):
    print('1 ~ 100 사이의 숫자를 입력해주세요')
    continue
  else:
    break

print(sep='\n')

for i in range(1, num+1):
  print(num, sep='\n')
  num = num -1
