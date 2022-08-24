# 0이 입력될 때까지 무한 출력하기
# 정수는 순서대로 입력됨
# 단 몇 개가 입력되는지 알 수 없음
# 0 아니면 정수 출력, 0이면 출력 중단

def return_num():
  num = int(input())
  return num

while(1):
  i = return_num()  # input 함수

  if(i > 0 or i < 0):
    print(i, 10sep='\n'):
    continue
  else:
    break

